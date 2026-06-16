from django.shortcuts import render
import urllib.request
import urllib.parse
import urllib.error
import json
import datetime

def weather_dashboard(request):
    API_KEY = "9790e5aa6c3476ec3b3c0baf09acb481"
    
    # Get city from POST request, fallback to GET, fallback to default "Rajkot"
    city = request.POST.get('city', request.GET.get('city', 'Rajkot')).strip()
    if not city:
        city = 'Rajkot'
        
    weather_data = None
    error_message = None
    
    try:
        # Encode city name for URL
        encoded_city = urllib.parse.quote(city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={API_KEY}"
        
        # Build Request with User-Agent
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # Extract and process weather details
            timezone_offset = data.get('timezone', 0)
            
            # Helper function to convert UTC UNIX timestamp to city local time format
            def format_local_time(timestamp):
                utc_time = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
                local_time = utc_time + datetime.timedelta(seconds=timezone_offset)
                return local_time.strftime('%I:%M %p')
                
            # Current time in city local time
            utc_now = datetime.datetime.now(datetime.timezone.utc)
            local_now = utc_now + datetime.timedelta(seconds=timezone_offset)
            current_date_str = local_now.strftime('%A, %b %d, %Y')
            current_time_str = local_now.strftime('%I:%M %p')

            weather_data = {
                'city': data.get('name'),
                'country': data.get('sys', {}).get('country'),
                'temp': round(data.get('main', {}).get('temp', 273.15) - 273.15, 1),
                'feels_like': round(data.get('main', {}).get('feels_like', 273.15) - 273.15, 1),
                'temp_min': round(data.get('main', {}).get('temp_min', 273.15) - 273.15, 1),
                'temp_max': round(data.get('main', {}).get('temp_max', 273.15) - 273.15, 1),
                'humidity': data.get('main', {}).get('humidity'),
                'pressure': data.get('main', {}).get('pressure'),
                'visibility': round(data.get('visibility', 0) / 1000, 1), # convert meters to km
                'wind_speed_ms': data.get('wind', {}).get('speed', 0),
                'wind_speed_kmh': round(data.get('wind', {}).get('speed', 0) * 3.6, 1), # convert m/s to km/h
                'wind_deg': data.get('wind', {}).get('deg', 0),
                'description': data.get('weather', [{}])[0].get('description', '').title(),
                'main_desc': data.get('weather', [{}])[0].get('main', ''),
                'icon': data.get('weather', [{}])[0].get('icon', '01d'),
                'sunrise': format_local_time(data.get('sys', {}).get('sunrise', 0)),
                'sunset': format_local_time(data.get('sys', {}).get('sunset', 0)),
                'current_date': current_date_str,
                'current_time': current_time_str,
            }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            error_message = f"City '{city}' not found. Please check spelling and try again."
        elif e.code == 401:
            error_message = "Invalid API Key. Please verify your OpenWeatherMap credentials."
        else:
            error_message = f"Weather service returned an error (HTTP {e.code}). Please try again later."
    except urllib.error.URLError as e:
        error_message = "Network connection failed. Please ensure you are connected to the internet."
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        
    context = {
        'weather_data': weather_data,
        'error_message': error_message,
        'search_query': city
    }
    
    return render(request, 'weather/dashboard.html', context)

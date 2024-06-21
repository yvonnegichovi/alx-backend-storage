#!/usr/bin/env python3
"""
This module implements an expiring web cache and tracker
"""

redis_client = redis.Redis()

def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a URL is accessed."""
    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs):
        redis_client.incr(f"count:{url}")
        return method(url, *args, **kwargs)
    return wrapper

def cache_page(method: Callable) -> Callable:
    """Decorator to cache the HTML content of a URL."""
    @functools.wraps(method)
    def wrapper(url: str, *args, **kwargs):
        cache_key = f"cache:{url}"
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')
        html_content = method(url, *args, **kwargs)
        redis_client.setex(cache_key, 10, html_content)
        return html_content
    return wrapper

@count_calls
@cache_page
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and cache the result."""
    response = requests.get(url)
    return response.text

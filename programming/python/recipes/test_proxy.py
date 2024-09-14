def test_proxy():
    import time
    from json import loads
    from requests import get   
    
    
    ips = "128.199.221.231:9999"
    proxies = { 
            'http': 'socks5://{}'.format(ips), 
            'https': 'socks5://{}'.format(ips)
            }


    request_result = get("http://ifconfig.me", proxies=proxies, timeout=5)
    print(request_result) 
    print(request_result.text) 
                    
test_proxy()      
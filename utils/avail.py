import whois

def is_available(domain):
    try:
        w = whois.whois(domain)
        return False
    except:
        return domain

import whois

def getDomainInfo():
    # ask the user to enter a domain to get info
    domain = input("Please enter a domain/website to get information about it: ")
    # use whois method to get the domain information
    information = whois.whois(domain)
    print(information)
    # to get particular information deal with "information" variable as dictionary data type.
    print('Name:', information['name'])
    print('Country:', information['country'])
    print('Email', information['emails'])

getDomainInfo()

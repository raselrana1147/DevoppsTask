url_list = [
    "http://mail.yahoo.com/inbox",
    "https://docs.github.com/en/actions",
    "https://support.apple.com/iphone",

]
domain_list=[]
for url in url_list:
    host = url.split("://")[-1].split("/")[0]   # get full host
    main_domain = ".".join(host.split(".")[-2:])  # keep last two parts
    domain_list.append(main_domain)

print(domain_list)


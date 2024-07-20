import api, logger

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def parse_coins():
    logging = logger.Logger('[INFO]')
    
    depths = api.get_exchange_info()
    symbols = depths['symbols']
    sp = []
    
    logging.log(f'Started sorting {len(symbols)} coins.')
    
    for i in range(len(symbols)):
        if str(symbols[i]['symbol'])[-4:] == 'USDT' and symbols[i]['status'] == 'TRADING':
            sp.append(symbols[i]['symbol'])
            
    logging.log('Ended parsing.')
            
    return sp
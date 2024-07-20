import time
import api, others, logger

def main():
    logging = logger.Logger("[OUT]")
    
    symbols = others.parse_coins()
    
    cnt_bid = 0
    cnt_ask = 0
    cnt_leftover_time = 0
    
    list_of_anom_bid = []
    list_of_anom_ask = []
    
    for sym in symbols:
        if cnt_leftover_time % 30 == 0:
            time.sleep(3)
            
        depth = api.get_order_book(symbol=f"{sym}", limit=1000)
        # price = get_ticker_price(symbol=f"{sym}")
        
        ask = depth['asks']
        bid = depth['bids']
        
        final_bid = 0
        final_ask = 0

        for i in range(1000):
            try:
                if float(bid[i][0]) / float(bid[0][0]) < 0.97 and float(ask[0][0]) / float(ask[i][0]) < 0.97:
                    # logging.log(f'{sym}')
                    break
                else:
                    if float(bid[i][0]) / float(bid[0][0]) >= 0.97:
                        final_bid += float(bid[i][1]) * float(bid[i][0])
                    if float(ask[0][0]) / float(ask[i][0]) >= 0.97:
                        final_ask += float(ask[i][1]) * float(ask[i][0])
            except:
                break
            
        if final_bid / final_ask >= 4:
            list_of_anom_bid.append(sym)

        if final_ask / final_bid >= 4:
            list_of_anom_ask.append(sym)
            
        cnt_bid += final_bid
        cnt_ask += final_ask
        cnt_leftover_time += 1
            
    logging.log(f'total bid (go long): {others.human_format(int(cnt_bid))}')
    logging.log(f'total ask (go short): {others.human_format(int(cnt_ask))}')
    logging.log(f'anom bid: {list_of_anom_bid}')
    logging.log(f'anom ask: {list_of_anom_ask}')
            
if __name__ == '__main__':
    main()
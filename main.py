import http.client
import json
# import matplotlib.pyplot as plt
import pandas as pd

first_df = pd.DataFrame()
for x in range(27):
    print('processing page: ', x)
    conn = http.client.HTTPSConnection("vn.investing.com")
    payload = 'country%5B%5D=178&sector=33%2C26%2C31%2C36%2C35%2C28%2C27%2C25%2C24%2C34%2C32%2C29%2C30&industry=181%2C185%2C202%2C197%2C206%2C213%2C220%2C208%2C224%2C225%2C222%2C223%2C189%2C211%2C191%2C186%2C195%2C204%2C219%2C221%2C187%2C188%2C232%2C180%2C229%2C226%2C193%2C177%2C173%2C178%2C183%2C217%2C212%2C205%2C198%2C210%2C230%2C175%2C218%2C227%2C201%2C194%2C172%2C215%2C209%2C174%2C216%2C228%2C200%2C214%2C196%2C231%2C203%2C176%2C182%2C179%2C192%2C184%2C190%2C207%2C199&equityType=ORD%2CDRC%2CPreferred%2CUnit%2CClosedEnd%2CREIT%2CELKS%2COpenEnd%2CRight%2CParticipationShare%2CCapitalSecurity%2CPerpetualCapitalSecurity%2CGuaranteeCertificate%2CIGC%2CWarrant%2CSeniorNote%2CDebenture%2CETF%2CADR%2CETC&exchange%5B%5D=122&exchange%5B%5D=72&pn=' + x.__str__() + '&order%5Bcol%5D=eq_market_cap&order%5Bdir%5D=d'
    headers = {
        'authority': 'vn.investing.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'udid=de73220ce3de80297b34d2f8372e8621; user-browser-sessions=1; browser-session-counted=true; SideBlockUser=a%3A1%3A%7Bs%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A958399%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A32%3A%22%2Fequities%2Fbinh-dinh-minerals-jsc%22%3B%7D%7D%7D%7D; pm_score=clear; _gid=GA1.2.1430408086.1674726944; __gads=ID=24ecf9647f100117:T=1674726943:S=ALNI_MbEywUfhnJidIU4WgAj_cpoBaPFOA; _pbjs_userid_consent_data=3524755945110770; _lr_env_src_ats=false; panoramaId_expiry=1675331746603; _cc_id=fadc8e8bdce6773fc7f697b22bac0c04; panoramaId=2b56342008cd747b29e04e4acaf316d53938e8b41b786e40d52716ba5e2d4b2f; pbjs-unifiedid=%7B%22TDID%22%3A%22e07a6633-150f-4f87-8132-bf379a34077f%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-12-26T09%3A55%3A46%22%7D; PHPSESSID=18jesfr02cuck19eidt17otrbo; adBlockerNewUserDomains=1674727013; _fbp=fb.1.1674727019008.538229614; G_ENABLED_IDPS=google; r_p_s_n=1; protectedMedia=2; pms={"f":2,"s":2}; adsFreeSalePopUp=3; _hjSessionUser_174945=eyJpZCI6IjQ3YTlkNDU3LTNjMjctNWVhNy05OTNlLTYzY2EwY2I5Y2JhNSIsImNyZWF0ZWQiOjE2NzQ3MjY5NDM0NDMsImV4aXN0aW5nIjp0cnVlfQ==; g_state={"i_p":1674831622453,"i_l":2}; __gpi=UID=00000bad904d4178:T=1674726943:RT=1674810439:S=ALNI_MaXqB28SegQQGRNn6l07We7yGQ6fA; smd=de73220ce3de80297b34d2f8372e8621-1674812480; geoC=VN; __cflb=02DiuF9qvuxBvFEb2q9QUGzowXC8RPhraZ1nKjyjYjeh2; _lr_retry_request=true; pbjs-unifiedid_last=Fri%2C%2027%20Jan%202023%2009%3A49%3A32%20GMT; __cf_bm=53cao3s8i5pDGge6nMLnSsxsL6pGntc3pWdjCHYcy2A-1674813014-0-AQg+7i8dYm8d9T5aDgbZo9d3eNjulX143SyqdoDGHcVIKP6Ge4NdGpUpfidqg1s2bYjiv09UMOnIbhfelE+0I3Y=; _hjSession_174945=eyJpZCI6ImMxMDA0MzUxLTc2MGQtNDA1YS05ZWVjLWFkN2UxNDJhYjQwZSIsImNyZWF0ZWQiOjE2NzQ4MTMxMjYzMDgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; nyxDorf=Z2NlNmIwPnw%2FaDs1NG40KD9vM2BlfDU1YWVvbw%3D%3D; _ga_C4NDLGKVMK=GS1.1.1674812968.3.1.1674813200.60.0.0; invpc=19; _ga=GA1.2.331460307.1674726943; page_view_count=18; smd=de73220ce3de80297b34d2f8372e8621-1674812480; udid=de73220ce3de80297b34d2f8372e8621; PHPSESSID=18jesfr02cuck19eidt17otrbo',
        'origin': 'https://vn.investing.com',
        'referer': 'https://vn.investing.com/stock-screener/?sp=country::178|sector::a|industry::a|equityType::a|exchange::72%3Ceq_market_cap;2',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    conn.request("POST", "/stock-screener/Service/SearchStocks", payload, headers)
    res = conn.getresponse()
    data = res.read()

    json_data = data.decode("utf-8")
    data_payload = json.loads(json_data)
    df = pd.json_normalize(data_payload['hits'])
    first_df = pd.concat([first_df, df], axis=0)

# df1 = pd.DataFrame(data_payload['hits'])
# print(df1.iloc[[0, 2, 4],[0,1]])
# print(df1.columns)
# print(df1.iloc[0:25,[0,1]])
# print(df1.loc[0:25,'last':'a52_week_low_frmt'])


# first_df['sector_trans'].value_counts().plot(kind='pie')
# plt.show()
first_df.to_csv('full_5.csv', encoding='utf-8', index=False)

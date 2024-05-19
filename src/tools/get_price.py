class PriceRetriever:
    def __init__(self):
        self.urls = {
            "elite": "https://www.cult.fit/fitness/cultpass-elite",
            "pro": "https://www.cult.fit/fitness/cultpass-pro",
            "default": "https://www.cult.fit/lp/Elite_lp_sale?utm_source=google&utm_medium=search_TCPA&utm_vertical=elite&utm_campaign=Cult_Search_Unified_Offline_Brand_Elite&Pro_TCPA&utm_adg=154756465800&utm_ad=669347628440&utm_kd=cult.fit&utm_mt=e&utm_adp=&utm_gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8rZkkog4qcflUhZH6HSO3aoCV-AQ8OKBkAKsFbKRreW4rUuIEv3UTIaAj-DEALw_wcB&utm_d=c&utm_dm=&gad_source=1&gclid=Cj0KCQjw3ZayBhDRARIsAPWzx8rZkkog4qcflUhZH6HSO3aoCV-AQ8OKBkAKsFbKRreW4rUuIEv3UTIaAj-DEALw_wcB"
        }
    
    def get_price(self, query:str):
        query_lower = query.lower()
        if 'elite' in query_lower:
            return f"You can see the details here: {self.urls['elite']}"
        elif 'pro' in query_lower:
            return f"You can see the details here: {self.urls['pro']}"
        return f"You can see the details here: {self.urls['default']}"

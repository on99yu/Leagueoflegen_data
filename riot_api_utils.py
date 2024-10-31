import time
import requests
import json
class api_utils:
    def __init__(self,api_key):
        self.REQUEST_HEADERS={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": api_key
        }
        self.req_count = 0

    def request_timer(self):
        self.req_count +=1
        if self.req_count % 100 == 0:
            print("api 요청 횟수 제한 : 대기중")
            time.sleep(120)
        else:
            time.sleep(1)
    # 상위랭크 소환사 아이디 리스트
    def get_challenger_list(self):
        self.request_timer()
        url = "https://kr.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        usr_list = response.json()['entries']
        return usr_list
    def get_grandmaster_list(self):
        self.request_timer()
        url = "https://kr.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        usr_list = response.json()['entries']
        return usr_list
    def get_master_list(self):
        self.request_timer()
        url = "https://kr.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        usr_list = response.json()['entries']
        return usr_list
    
    # puuid 구하기
    def get_puuid(self, encryptedSummonerId):
        self.request_timer()
        url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/{encryptedSummonerId}"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        puuid = response.json()["puuid"]
        return puuid
    
    # 매치리스트 구하기
    def get_match_list(self,puuid, count):
        self.request_timer()
        url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&queue=420"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        match_list =response.json()
        return match_list

    def get_match_info(self,match_id):
        self.request_timer()
        url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        match_info = response.json()
        return match_info

    def get_match_timeline(self,match_id):
        self.request_timer()
        url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline"
        response = requests.get(url, headers=self.REQUEST_HEADERS)
        match_timeline = response.json()
        return match_timeline
    
    def get_champion_info(self):
        url ="https://ddragon.leagueoflegends.com/cdn/14.21.1/data/en_US/champion.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"요청 실패: {response.status_code}")
        return data
    
    def get_item_info(self):
        url ="https://ddragon.leagueoflegends.com/cdn/14.21.1/data/en_US/item.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"요청 실패: {response.status_code}")
        return data
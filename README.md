# How to use
## Environment setup
```pip install -r requirements.txt```

## Config setup
안내하는 대로 SENDGRID_API_KEY 토큰을 .env 파일에 추가.

## Crawling
```python3 crawl.py```

날짜 입력하라는 프롬프트가 뜰 텐데, YYYY-MM-DD 양식에 맞게 기준일 입력.

(이 날짜 이후로 업데이트된 회사는 추가/변경으로 알아서 분류해서 취급하니 날짜가 틀리지 않도록 주의!)

## Sending emails
```python3 send_emails.py --settings=test```

info@snaac.co.kr로만 이메일 발송하는 테스트용 함수!

```python3 send_emails.py --settings=prod```

recipients.json에서 받는 이 정보를 받아옴!

recipients.json 양식은 다음과 같음.
```
{
    "황진우": "luorix@snu.ac.kr"
}
```
이름은 안 중요한데, 식별용으로 받고 있음.
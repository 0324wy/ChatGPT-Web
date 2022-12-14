# ChatGPT-Web
I build a web server of chatGPT based on [ChatGPT](https://github.com/acheong08/ChatGPT). You can use it to build your web application.

# Features
![image](https://user-images.githubusercontent.com/36258159/205534498-acc59484-c4b4-487d-89a7-d7b884af709b.png)
- No moderation
- Programmable

# Setup
## Install
`pip3 install revChatGPT --upgrade`

## Email and password authentication
```json
{
    "email": "<YOUR_EMAIL>",
    "password": "<YOUR_PASSWORD>"
}
```
Save this in `config.json` in current working directory

<details>
<summary>

## Token Authentication
</summary>
Go to https://chat.openai.com/chat and log in or sign up

1. Open console with `F12`
2. Open `Application` tab > Cookies
![image](https://user-images.githubusercontent.com/36258159/205494773-32ef651a-994d-435a-9f76-a26699935dac.png)
3. Copy the value for `__Secure-next-auth.session-token` and paste it into `config.json.example` under `session_token`. You do not need to fill out `Authorization`
![image](https://user-images.githubusercontent.com/36258159/205495076-664a8113-eda5-4d1e-84d3-6fad3614cfd8.png)
4. Save the modified file to `config.json` (In the current working directory)
</details>

# Running
```
 $ python3 -m revChatGPT
```

Refresh every so often in case the token expires.

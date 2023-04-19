#!/bin/bash
curl 'https://www.stoningtoncountryclub.com/api/v1/teetimes/CommitBooking/0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Cookie: CMSPreferredCulture=en-US; CMSCookieLevel=1000; CMSPreferredUICulture=en-us; .ASPXFORMSAUTH=A2394A75E497892A8CCDF423B601CBD4ECE95DD200EF32087A6823CB3BF0E6D82A84A92CE197E455F705300A4DF3B4F06EF8993A5702FEA4CE49446F696FBFB0C9C32B26642431F64D75DAC5A969F8D349AD1CC3F28F86C3C14996E5B70351B6284BAFFBB2E0B2814EA73827043A9DF93AF33CC84ED3F8AD05D4645CDD1B7927278B5373DD21FC9437B53D01EDC6CC0168457798; u53Rn3yM=ZHlsYW5rcmlzaA==; ASP.NET_SessionId=j3euyp1j3g53zx1krs1xnelf; JNS=2204543168.20480.0000' \
  -H 'Origin: https://www.stoningtoncountryclub.com' \
  -H 'Referer: https://www.stoningtoncountryclub.com/CMSModules/CHO/TeeTimes/TeeTimes.aspx' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-GPC: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"Mode":"Booking","BookingId":0,"OwnerId":1004130383,"editingBookingId":null,"Reservations":[{"ReservationId":0,"ReservationType":0,"FullName":"Dylan Krishnan","Transport":"0","Caddy":"false","Rentals":"","MemberId":1004130383}],"Holes":18,"StartingHole":"1","wait":false,"Allowed":null,"enabled":true,"startTime":null,"endTime":null,"Notes":""}' \
  --compressed
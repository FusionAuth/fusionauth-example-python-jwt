import datetime
import python_jwt as jwt
import jwcrypto.jwk as jwk

def run(): 
  key = jwk.JWK.generate(kty='RSA', size=2048)

  # User API
  
  
  payload = { "iss": "fusionauth.io", 
              "aud": "238d4793-70de-4183-9707-48ed8ecd19d9",
              "sub": "19016b73-3ffa-4b26-80d8-aa9287738677",
              "name": "Dan Moore",
              "roles": ["RETRIEVE_TODOS"]
  }
  
  encoded = jwt.generate_jwt(payload, key, "RS256", datetime.timedelta(minutes=5))
  
  print(encoded)
  
  # Todo  API
  decoded = jwt.verify_jwt(encoded, key, ["RS256"])
  
  print(decoded)

from app import hmac,rsa,hmac_verify_claims
import sys

if __name__ == "__main__":
  print(sys.argv[1])
  if sys.argv[1] == "hmac": 
    hmac.run()
  if sys.argv[1] == "rsa": 
    rsa.run()
  if sys.argv[1] == "hmac_verify_claims": 
    hmac_verify_claims.run()

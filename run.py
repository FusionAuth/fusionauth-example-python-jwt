from app import hmac, rsa, hmac_verify_claims, rsa_wrong_algo
import sys

if __name__ == "__main__":
  if sys.argv[1] == "hmac": 
    hmac.run()
  if sys.argv[1] == "rsa": 
    rsa.run()
  if sys.argv[1] == "hmac_verify_claims": 
    hmac_verify_claims.run()
  if sys.argv[1] == "rsa_wrong_algo": 
    rsa_wrong_algo.run()

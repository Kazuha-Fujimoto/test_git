import validators
import re

def validate_domain(domain):
      '''
      ドメイン許可の設定値をバリデーション
      例: .example.com, example.com, *.example.com
      '''
      if not domain or not isinstance(domain, str):
          return False, "ドメインが空です"
      
      domain = domain.strip()
      
      # ワイルドカード形式
      #if domain.startswith('*.'):
      #    domain = domain[2:]
      #elif domain.startswith('.'):
      #    domain = domain[1:]
      
      # ワイルドカード削除後に空の場合
      #if not domain:
      #    return False, "ドメイン部分が空です"
    
      # ドメインのバリデーション
      if validators.domain(domain):
          return True, "OK"	
      else:
          return False, "無効なドメイン形式です"     

# テストコード
if __name__ == "__main__":
    test_domains = [
        ".example.com",
        "example.com",
        "*.example.com",
        "sub.example.com",
        "invalid_domain",
        "",
        "   ",
        "*.invalid_domain",
        ".",
        "*.",
    ]
    
    for domain in test_domains:
        is_valid, message = validate_domain(domain)
        print(f"Domain: '{domain}' => Valid: {is_valid}, Message: '{message}'")
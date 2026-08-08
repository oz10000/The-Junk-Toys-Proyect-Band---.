# scripts/console_ranking.py
import sys
sys.path.insert(0, '.')
from application.use_cases.scan_market import ScanMarket

def main():
    scanner = ScanMarket()
    result = scanner.execute()
    print("\n🏆 RANKING DE SEÑALES")
    print("=" * 50)
    for i, item in enumerate(result['ranking'][:10]):
        signal = item['signal']
        print(f"{i+1}. {signal.symbol} {signal.direction.value} Score: {signal.score.value:.3f}")
    print("=" * 50)

if __name__ == '__main__':
    main()
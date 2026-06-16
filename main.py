from analyzer import generate_report

def main():
    print("="*50)
    print("          WebSec - Web Security Analyzer")
    print("="*50)

    url = input("Enter the URL to analyze: ")
    report = generate_report(url)
    
    print("\n--- Security Analysis Report ---")
    print(f"URL: {report['URL']}")
    print("\nSecurity Headers:")
    for header, present in report["Security Headers"].items():
        status = "Present" if present else "Missing"
        print(f"  {header}: {status}")
    
    print(f"\nHTTPS: {'Yes' if report['HTTPS'] else 'No'}")
    print(f"Robots.txt: {'Found' if report['Robots.txt'] else 'Not Found'}")
    print(f"Security.txt: {'Found' if report['Security.txt'] else 'Not Found'}")
    
    if report["Common Directories"]:
        print("\nCommon Directories Found:")
        for directory in report["Common Directories"]:
            print(f"  - {directory}")
    else:
        print("\nNo common directories found.")
    
main()
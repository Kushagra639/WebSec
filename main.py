from analyzer import generate_report

def main():
    print("="*50)
    print("          WebSec - Web Security Analyzer")
    print("="*50)

    url = input("Enter the URL to analyze: ")
    report = generate_report(url)
    
    if "Error" in report:
        print(f"\nError: {report['Error']}")
        return
    else:
        print("\n--- Security Analysis Report ---")
        print(f"\nURL: {report['URL']}")
        print(f"Server: {report['Server']}")
        print("\nSecurity Headers:")
        for header, present in report["Security Headers"].items():
            status = "Present" if present else "Missing"
            print(f"  {header}: {status}")
        
        print(f"\nHTTPS: {'Yes' if report['HTTPS'] else 'No'}")
        print(f"HTTP Status Code: {report['HTTP Status Code']}")
        print(f"Robots.txt: {'Found' if report['Robots.txt'] else 'Not Found'}")
        print(f"Security.txt: {'Found' if report['Security.txt'] else 'Not Found'}")
        
        if report["Common Directories"]:
            print("\nCommon Directories Found:")
            for directory in report["Common Directories"]:
                print(f"  - {directory}")
        else:
            print("\nNo common directories found.")
        if report["Redirects"]:
            print("\nRedirects:")
            for redirect in report["Redirects"]:
                print(f"  - {redirect}")
        else:
            print("\nNo redirects found.")

while True:
    main()
    const = input("\nDo you want to analyze another URL? (y/n): ")
    if const.lower() != 'y':
        print("Exiting WebSec Analyzer. Stay secure!")
        break 

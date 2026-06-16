from analyzer import generate_report
import customtkinter as ctk
from tkinter import messagebox
from pathlib import Path
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

home_dir = Path.home()
downloads_dir = home_dir / "Downloads"
report_file = downloads_dir / f"websec_report_{timestamp}.txt"
theme_file = Path(__file__).parent / "pastel_theme.json"

ctk.set_appearance_mode("system")
ctk.set_default_color_theme(str(theme_file)) # Sets the default color theme to a custom pastel theme (given alongside this code), please change the path to the theme file as per your system

app = ctk.CTk()
app.title("WebSec - Web Security Analyzer 🔐") 
app.geometry("900x700") 
app.resizable(width=True, height=True)

def create_bottom_frame():
    bottom_frame = ctk.CTkFrame(master=app)
    bottom_frame.pack(side='bottom', fill='x',padx=20, pady=10)
    return bottom_frame

def change_theme(): # Function to toggle between light and dark themes
    try:
        if ctk.get_appearance_mode() == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")
    except Exception as e:
        print(f" ❌ Error changing theme: {e}")
        messagebox.showerror("Theme Error", f"Error changing theme: {e}")

def clear_screen(): # Function to clear the current screen by destroying all widgets in the main application window
    try:
        for widget in app.winfo_children():
            widget.destroy()
    except Exception as e:
        print(f" ❌ Error clearing screen: {e}")
        messagebox.showerror("Screen Error", f"Error clearing screen: {e}")

def main_menu():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Welcome to WebSec!", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        options = [
            "Analyze URL", "Exit"
        ]
        for idx, opt in enumerate(options, 1):
            ctk.CTkButton(app, text=f"{idx}. {opt}", command=lambda i=idx: option_selected(i)).pack(pady=4) # Creates buttons for each option in the main menu
        
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in main menu: {e}")
        messagebox.showerror("Menu Error", f"Error in main menu: {e}")

def buffer_screen(url):
    try:
        clear_screen()

        ctk.CTkLabel(app, text="Loading...", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        
        def load_report():
            analysis_report_screen(url)

        app.after(10, load_report)

    except Exception as e:
        print(f" ❌ Error in buffer screen: {e}")
        messagebox.showerror("Buffer Screen Error", f"Error in buffer screen: {e}")

def analysis_report_screen(url): # Function to display the analysis report in a new window after analyzing a URL
    try:
        clear_screen()

        main_frame = ctk.CTkScrollableFrame(master=app)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(main_frame, text="Analysis Report", font=ctk.CTkFont(size=32, weight="bold")).pack(pady=10)

        report = generate_report(url)
        if "Error" in report:
            messagebox.showerror("Analysis Error", f"Error analyzing URL: {report['Error']}")
            main_menu()
            return

        ctk.CTkLabel(main_frame, text=f"URL: {report['URL']}").pack(pady=5)
        ctk.CTkLabel(main_frame, text=f"Server: {report['Server']}").pack(pady=2)

        ctk.CTkLabel(main_frame, text="Security Headers:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        for header, present in report["Security Headers"].items():
            status = "Present" if present else "Missing"
            ctk.CTkLabel(main_frame, text=f"{header}: {status}", text_color="green" if present else "red").pack(pady=1)

        ctk.CTkLabel(main_frame, text=f"HTTPS: {'Yes' if report['HTTPS'] else 'No'}").pack(pady=2)
        ctk.CTkLabel(main_frame, text=f"HTTP Status Code: {report['HTTP Status Code']}").pack(pady=2)
        ctk.CTkLabel(main_frame, text=f"Robots.txt: {'Found' if report['Robots.txt'] else 'Not Found'}").pack(pady=2)
        ctk.CTkLabel(main_frame, text=f"Security.txt: {'Found' if report['Security.txt'] else 'Not Found'}").pack(pady=2)

        if report["Common Directories"]:
            ctk.CTkLabel(main_frame, text="Common Directories Found:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
            for directory in report["Common Directories"]:
                ctk.CTkLabel(main_frame, text=f"- {directory}").pack(pady=1)
        else:
            ctk.CTkLabel(main_frame, text="No common directories found.", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        if report["Redirects"]:
            ctk.CTkLabel(main_frame, text="Redirects:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
            for redirect in report["Redirects"]:
                ctk.CTkLabel(main_frame, text=f"- {redirect}").pack(pady=1)
        else:
            ctk.CTkLabel(main_frame, text="No redirects found.", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
        
        def export_report():
            try:
                with open(report_file, "w") as f:
                    f.write("="*49 + "\n")
                    f.write("      WebSec - Web Security Analyzer Report      \n")
                    f.write("="*49 + "\n\n")
                    f.write(f"URL: {report['URL']}\n")
                    f.write(f"Server: {report['Server']}\n\n")
                    f.write("Security Headers:\n")
                    for header, present in report["Security Headers"].items():
                        status = "Present" if present else "Missing"
                        f.write(f"  {header}: {status}\n")
                    f.write(f"\nHTTPS: {'Yes' if report['HTTPS'] else 'No'}\n")
                    f.write(f"HTTP Status Code: {report['HTTP Status Code']}\n")
                    f.write(f"Robots.txt: {'Found' if report['Robots.txt'] else 'Not Found'}\n")
                    f.write(f"Security.txt: {'Found' if report['Security.txt'] else 'Not Found'}\n\n")
                    if report["Common Directories"]:
                        f.write("Common Directories Found:\n")
                        for directory in report["Common Directories"]:
                            f.write(f"  - {directory}\n")
                    else:
                        f.write("No common directories found.\n")
                    if report["Redirects"]:
                        f.write("\nRedirects:\n")
                        for redirect in report["Redirects"]:
                            f.write(f"  - {redirect}\n")
                    else:
                        f.write("\nNo redirects found.\n")
                messagebox.showinfo("Export Successful", f"Report exported successfully to: {report_file}")
            except Exception as e:
                print(f" ❌ Error exporting report: {e}")
                messagebox.showerror("Export Error", f"Error exporting report: {e}")
        
        ctk.CTkButton(main_frame, text="Export Report", command=export_report).pack(pady=10)

        ctk.CTkButton(bottom_frame, text="Back", command=lambda: analyze_url_screen()).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in analysis report screen: {e}")
        messagebox.showerror("Report Screen Error", f"Error in analysis report screen: {e}")
        


def analyze_url_screen():
    try:
        clear_screen()

        bottom_frame = create_bottom_frame()

        ctk.CTkLabel(app, text="Enter URL to Analyze", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        url_entry = ctk.CTkEntry(app, width=400, placeholder_text="https://example.com")
        url_entry.pack(pady=5)

        def analyze():
            url = url_entry.get()
            if not url:
                messagebox.showerror("Input Error", "Please enter a URL.")
                return
            buffer_screen(url)

        ctk.CTkButton(app, text="Analyze", command=analyze).pack(pady=10)
        ctk.CTkButton(bottom_frame, text="Back", command=lambda: main_menu()).pack(side='left', pady=5)
        ctk.CTkButton(bottom_frame, text="Change Theme", command=change_theme).pack(side='right', pady=5)
    except Exception as e:
        print(f" ❌ Error in analyze URL screen: {e}")
        messagebox.showerror("Analyze Screen Error", f"Error in analyze URL screen: {e}")

def option_selected(option): # Function to handle the option selected by the user in the main menu
    try:
        if option == 1:
            analyze_url_screen()
        elif option == 2:
            app.destroy()
        else:
            messagebox.showerror("Error", "Invalid option selected.")
            main_menu()
    except Exception as e:
        print(f" ❌ Error in option selection: {e}")
        messagebox.showerror("Option Selection Error", f"Error in option selection: {e}")

main_menu() # Start the application by displaying the main menu
app.mainloop()
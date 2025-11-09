"""
Sample application for multi-platform matrix build demonstration
"""

def main():
    print("Multi-Platform Matrix Build Demo")
    print("=" * 40)
    print("This application runs on multiple platforms:")
    print("- Ubuntu (Linux)")
    print("- macOS")
    print("- Windows")
    print("=" * 40)
    
    import sys
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")

if __name__ == "__main__":
    main()

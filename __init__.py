from generate_pass import GeneratePassword
import argparse

if __name__ == "__main__":
    g  = GeneratePassword()

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--interval', type=int, help='time interval in seconds')
    parser.add_argument('--generate_passwords', action='store_true', help='generate passwords')

    args = parser.parse_args()

    if args.generate_passwords:
        if args.interval is None:
            parser.error('time interval is required')
        else:
            g.generatePasswordOnInterval(args.interval)
            print(f'passwords generated successfully')
    else:
        parser.print_help()
   
    
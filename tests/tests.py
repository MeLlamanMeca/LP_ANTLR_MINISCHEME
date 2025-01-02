import os
import argparse 

def run_tests(silent=False):
    all_passed = True
    input_dir = 'tests/input/'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, 'input/')
    output_dir = os.path.join(script_dir, 'output/')
    test_files = [f for f in os.listdir(input_dir) if f.endswith('.scm')]
    print("----------------------------------------")
    def run_single_test(input_file, output_file, test_name):
        with open(input_file, 'r'), open(output_file, 'r') as out:
            expected_output = out.read()
            actual_output = os.popen(f'python3 scheme.py {input_file}').read()
            test_name = test_name + ':'
            if actual_output == expected_output:
                print(f'{test_name:<30} \033[92mPASSED\033[0m')
            else:
                nonlocal all_passed
                all_passed = False
                print(f'{test_name:<30} \033[91mFAILED\033[0m')
                if not silent:
                    print(f'Expected:\n{expected_output}')
                    print(f'Actual:\n{actual_output}')

    for test_file in test_files:
        test_name = test_file[:-4]
        input_file = os.path.join(input_dir, test_file)
        output_file = os.path.join(output_dir, f'{test_name}.out')
        run_single_test(input_file, output_file, test_name)
    
    def run_iotest():
        iotest_input_file = os.path.join(script_dir, 'iotest/iotest.scm')
        iotest_output_file = os.path.join(script_dir, 'iotest/iotest.out')
        iotest_datain_file = os.path.join(script_dir, 'iotest/iotest.in')
        actual_output = os.popen(f'python3 scheme.py {iotest_input_file} < {iotest_datain_file}').read()
        with open(iotest_output_file, 'r') as out:
            expected_output = out.read()
        test_name = 'iotest:'
        if actual_output == expected_output:
            print(f'{test_name:<30} \033[92mPASSED\033[0m')
        else:
            nonlocal all_passed
            all_passed = False
            print(f'{test_name:<30} \033[91mFAILED\033[0m')
            if not silent:
                print(f'Expected:\n{expected_output}')
                print(f'Actual:\n{actual_output}')

    run_iotest()
    print("----------------------------------------")
    if all_passed:
        print('\033[42m' + ' ' * 40 + '\033[0m')
        print('\033[42m' + ' ' * 12 + 'TESTS SUCCEEDED' + ' ' * 13 + '\033[0m')
        print('\033[42m' + ' ' * 40 + '\033[0m')
    else:
        print('\033[41m' + ' ' * 40 + '\033[0m')
        print('\033[41m' + ' ' * 13 + 'TESTS FAILED' + ' ' * 15 + '\033[0m')
        print('\033[41m' + ' ' * 40 + '\033[0m')
        
                    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run tests with optional silent mode.')
    parser.add_argument('--silent', action='store_true', help='Run tests in silent mode')
    args = parser.parse_args()

    run_tests(silent=args.silent)
    
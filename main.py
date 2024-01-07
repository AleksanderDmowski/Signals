import engine

def main():
    engine.checking_compatibility_of_packages(fits_exe_relase= False, required_dir={'pandas', 'numpy'})
    engine.app().run()
    pass

if __name__ == '__main__':
    main()
 
import cx_Freeze

executables = [cx_Freeze.Executable("chromedino.py")]
buildOptions = dict(include_files = ['assets/', 'score.txt', 'requirements.txt']) 

cx_Freeze.setup(
    name="Chrome_dino_handmade",
    options=dict(build_exe = buildOptions),
    executables = executables

    )
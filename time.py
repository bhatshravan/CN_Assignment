
def bar(timeout):
    for i in range(timeout):
        time.sleep(1)

def timeout_fcn():
    p = multiprocessing.Process(target=bar)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(10)

    # If thread is still active
    if p.is_alive():
        print("running... let's kill it...")

        # Terminate
        p.terminate()
        p.join()
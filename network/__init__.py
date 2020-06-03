if __name__ == '__main__':

    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing

    q = multiprocessing.Manager().Queue()


    def put(val):
        q.put(val)


    with ProcessPoolExecutor() as p:
        for i in range(4):
            p.submit(put, i)

    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())

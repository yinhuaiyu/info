from redis import *
if __name__ == '__main__':
    try:
        sr = StrictRedis()
        result = sr.set('bb','itheima')
        print(result)
        get_result = sr.get('bb')
        print(get_result)
        result = sr.set('name', 'itcast')
        print(result)
        get_result1 = sr.get('name')
        print(get_result1)
        get_key =sr.keys()
        print(get_key)

    except Exception as e:
        print(e)
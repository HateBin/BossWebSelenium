import configparser, settings
import os


class IniRW:
    # 读取ini配置文件信息
    def Ini_Read(self, iniName, section, key):
        path = settings.BASE_DIR + '\config\{}.ini'.format(iniName)
        config = configparser.ConfigParser()
        config.read(path, encoding='utf-8')
        value = config[section][key]
        return value


    # 写入ini配置文件信息
    def Ini_Write(self, iniName, section, key, content):
        path = settings.BASE_DIR + '\config\{}.ini'.format(iniName)
        config = configparser.ConfigParser()
        config.read(path)
        config.set(section, key, content)
        # value = config[section][key]
        with open(path, 'w', encoding='utf-8') as f:
            config.write(f)
        # return value






if __name__ == '__main__':
    print(IniRW().Ini_Read(iniName='element_located', section='Login_Xpath', key='Account'))
    print(type(IniRW().Ini_Read(iniName='element_located', section='Login_Xpath', key='Account')))
    # print(IniRW().Ini_Write('Token', 'Authorization', '12345678'))
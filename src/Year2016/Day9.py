class Day9(object):
    @staticmethod
    def decrypt_v1(encrypted):
        decrypt = []
        index = 0
        while index < len(encrypted):
            if encrypted[index] == '(':
                end = encrypted.find(')', index) + 1
                number, repetition = map(int, encrypted[index + 1:end - 1].split('x'))
                decrypt = decrypt + list(encrypted[end:end + number] * repetition)
                index = end + number
            else:
                decrypt.append(encrypted[index])
                index += 1
        return ''.join(decrypt)

    @staticmethod
    def decrypt_v2(encrypted, store=False):
        decrypt = []
        index = 0
        count = 0
        while index < len(encrypted):
            if encrypted[index] == '(':
                end = encrypted.find(')', index) + 1
                number, repetition = map(int, encrypted[index + 1:end - 1].split('x'))
                if '(' in encrypted[end:end + number]:
                    sub_count, text = Day9.decrypt_v2(encrypted[end:end + number], store)
                    if store:
                        decrypt = decrypt + list(text * repetition)
                    count += repetition * sub_count
                else:
                    if store:
                        decrypt += encrypted[end:end + number] * repetition
                    count += number * repetition
                index = end + number
            else:
                if store:
                    decrypt.append(encrypted[index])
                index += 1
                count += 1

        return count, ''.join(decrypt)

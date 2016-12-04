from src import split_data

from collections import Counter
import re


class Day4(object):
    def is_room_valid(self, room):
        return self._process_room(room)[0]

    @split_data
    def sum_valid(self, rooms):
        return sum([sector_id for valid, sector_id, _ in self._process_rooms(rooms) if valid is True])

    @split_data
    def search(self, rooms, search):
        found_id = 0
        for (valid, sector_id, encrypted_room_name) in self._process_rooms(rooms):
            clear_text = self._decipher(encrypted_room_name, sector_id)
            if search in clear_text:
                found_id = sector_id
                break

        return found_id

    def _process_rooms(self, rooms):
        return [self._process_room(room) for room in rooms]

    def _process_room(self, room):
        encrypted_name = re.findall(r'(\w+)\-', room)
        sector_id = int(re.findall(r'(\d+)', room)[0])
        checksum = re.findall(r'\[(\w+)\]', room)[0] if len(re.findall(r'\[(\w+)\]', room)) == 1 else 0
        calculated_checksum = self._make_checksum(Counter(''.join(encrypted_name)))

        return checksum == calculated_checksum, sector_id, '-'.join(encrypted_name)

    def _make_checksum(self, counter):
        full_checksum = sorted(counter.items(), key=self._sort_number_and_letter)
        return ''.join([letter for letter, repetition in full_checksum[:5]])

    @staticmethod
    def _sort_number_and_letter(t):
        letter, number = t
        return -number, letter

    def _decipher(self, encrypted_room_name, sector_id):
        return ''.join(list(map(self._get_shift_caeser(sector_id), encrypted_room_name)))

    @staticmethod
    def _get_shift_caeser(sector_id):
        numbers = range(ord('a'), ord('z') + 1)
        move = sector_id % 26

        def shift_caeser(x):
            if x == '-':
                letter = ' '
            else:
                if ord(x) + move in numbers:
                    letter = chr(ord(x) + move)
                else:
                    letter = chr((ord(x) + move) % ord('z') + ord('a') - 1)
            return letter

        return shift_caeser

import struct

def convert_coordinates(file_path):
    """
    Конвертирует координаты в файле .sii из формата &ABCD в десятичный вид, сохраняя структуру файла.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            # Обрабатываем строку по символам
            converted_line = ''
            i = 0
            while i < len(line):
                if line[i] == '&':
                    coordinate_hex = line[i + 1: i + 9]  # Берем 8 символов после &
                    coordinate_bytes = bytes.fromhex(coordinate_hex)
                    coordinate_float = struct.unpack(">f", coordinate_bytes)[0]
                    converted_line += str(coordinate_float)
                    i += 9  # Переходим к следующему символу после координаты
                else:
                    converted_line += line[i]
                    i += 1
            # Удаляем лишний пробел в конце строки
            file.write(converted_line.rstrip() + '\n')  # Используем rstrip() для удаления пробелов в конце строки

if __name__ == "__main__":
    file_path = "landscape.game.sii"  # Замените на путь к вашему файлу .sii
    convert_coordinates(file_path)

    input("Нажмите любую клавишу, чтобы закрыть окно...")

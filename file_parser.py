import sys
from pathlib import Path

JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
HEIC_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
PY_FILES = []
C_FILES = []
HTML_FILES = []
PAGES_FILES = []
NUMBERS_FILES = []
KEY_FILES = []

OTHER_ITEMS = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'HEIC': HEIC_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
    'PY': PY_FILES,
    'C': C_FILES,
    'HTML': HTML_FILES,
    'PAGES': PAGES_FILES,
    'NUMBERS': NUMBERS_FILES,
    'KEY': KEY_FILES,
}


FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():
            # Перевіряємо, щоб папка не була тією в яку ми вже складаємо файли.
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other', 'files'):
                FOLDERS.append(item)
                scan(item)  # скануємо цю вкладену папку - рекурсія
            continue  # переходимо до наступного елемента в сканованій папці

        # Робота з файлом
        ext = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not ext:
            OTHER_ITEMS.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER_ITEMS.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')
    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Images heic: {HEIC_IMAGES}")
    print(f"Video avi: {AVI_VIDEO}")
    print(f"Video mp4: {MP4_VIDEO}")
    print(f"Video mov: {MOV_VIDEO}")
    print(f"Video mkv: {MKV_VIDEO}")
    print(f"Documents doc: {DOC_DOCUMENTS}")
    print(f"Documents docx: {DOCX_DOCUMENTS}")
    print(f"Documents txt: {TXT_DOCUMENTS}")
    print(f"Documents pdf: {PDF_DOCUMENTS}")
    print(f"Documents xlsx: {XLSX_DOCUMENTS}")
    print(f"Documents pptx: {PPTX_DOCUMENTS}")
    print(f"Audio mp3: {MP3_AUDIO}")
    print(f"Audio ogg: {OGG_AUDIO}")
    print(f"Audio wav: {WAV_AUDIO}")
    print(f"Audio amr: {AMR_AUDIO}")
    print(f"Archives zip: {ZIP_ARCHIVES}")
    print(f"Archives gz: {GZ_ARCHIVES}")
    print(f"Archives tar: {TAR_ARCHIVES}")
    print(f"Files py: {PY_FILES}")
    print(f"Files c: {C_FILES}")
    print(f"Files html: {HTML_FILES}")
    print(f"Files pages: {PAGES_FILES}")
    print(f"Files numbers: {NUMBERS_FILES}")
    print(f"Files key: {KEY_FILES}")
    print('-' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')
    print(f"Other files: {OTHER_ITEMS}")
    print(f"Folders: {FOLDERS}")

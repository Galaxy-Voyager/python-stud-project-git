from src.utils.logger import log_operation


def read_json_file(file_path: str):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            log_operation("Чтение файла", True, file=file_path)
            return data if isinstance(data, list) else []
    except Exception as e:
        log_operation("Чтение файла", False, error=str(e), file=file_path)
        return []

"""
stego_engine.py
LSB Steganography Engine for EIICS
"""

from PIL import Image

class StegoEngine:
    """LSB Steganography Engine"""
    
    @staticmethod
    def _bytes_to_binary(data: bytes) -> str:
        """Convert bytes to binary string"""
        return ''.join([f"{byte:08b}" for byte in data])

    @staticmethod
    def _binary_to_bytes(binary_str: str) -> bytes:
        """Convert binary string to bytes"""
        n = 8
        binary_str = binary_str[:len(binary_str) - (len(binary_str) % n)]
        byte_list = [int(binary_str[i:i+n], 2) for i in range(0, len(binary_str), n)]
        return bytes(byte_list)

    @staticmethod
    def calculate_capacity(image_path: str) -> int:
        """Calculate maximum data capacity in bytes"""
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                return (width * height * 3 - 32) // 8  # 32 bits for header
        except:
            return 0

    @staticmethod
    def embed_data(cover_image_path: str, secret_data: bytes, data_type: str, output_path: str) -> bool:
        """Embed data into image using LSB steganography"""
        try:
            image = Image.open(cover_image_path).convert('RGB')
            pixels = image.load()
            width, height = image.size

            # Create header
            data_type_header = b'TEXT' if data_type == 'text' else b'FILE'
            full_payload = data_type_header + secret_data
            payload_binary = StegoEngine._bytes_to_binary(full_payload)

            total_bits_needed = 32 + len(payload_binary)
            total_bits_available = width * height * 3

            if total_bits_needed > total_bits_available:
                raise ValueError(f"Data too large for image. Max capacity: {total_bits_available//8} bytes")

            data_to_embed = f"{len(payload_binary):032b}" + payload_binary
            data_index = 0

            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    for i, color_value in enumerate([r, g, b]):
                        if data_index < len(data_to_embed):
                            current_bit = data_to_embed[data_index]
                            new_color_value = (color_value & 0xFE) | int(current_bit)
                            if i == 0: r = new_color_value
                            elif i == 1: g = new_color_value
                            elif i == 2: b = new_color_value
                            data_index += 1
                    pixels[x, y] = (r, g, b)

            image.save(output_path, format='PNG')
            return True
            
        except Exception as e:
            raise Exception(f"Embedding failed: {str(e)}")

    @staticmethod
    def extract_data(stego_image_path: str) -> tuple:
        """Extract data from stego image"""
        try:
            image = Image.open(stego_image_path).convert('RGB')
            pixels = image.load()
            width, height = image.size

            # Extract length header
            length_binary = ''
            bits_extracted = 0
            
            for y in range(height):
                for x in range(width):
                    if bits_extracted >= 32:
                        break
                    r, g, b = pixels[x, y]
                    for color_value in [r, g, b]:
                        if bits_extracted < 32:
                            lsb = str(color_value & 1)
                            length_binary += lsb
                            bits_extracted += 1

            if len(length_binary) != 32:
                raise ValueError("Invalid image")

            payload_length = int(length_binary, 2)
            payload_binary = ''
            bits_extracted = 0

            for y in range(height):
                for x in range(width):
                    r, g, b = pixels[x, y]
                    for color_value in [r, g, b]:
                        if bits_extracted < (32 + payload_length):
                            if bits_extracted >= 32:
                                lsb = str(color_value & 1)
                                payload_binary += lsb
                            bits_extracted += 1

            payload_bytes = StegoEngine._binary_to_bytes(payload_binary)
            data_type_header = payload_bytes[:4]
            actual_data = payload_bytes[4:]

            if data_type_header == b'TEXT':
                data_type = 'text'
            elif data_type_header == b'FILE':
                data_type = 'file'
            else:
                raise ValueError("Invalid data type header")

            return data_type, actual_data

        except Exception as e:
            raise Exception(f"Extraction failed: {str(e)}")

if __name__ == "__main__":
    # Test the engine
    print("EIICS Stego Engine Test Complete")
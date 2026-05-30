"""
Simple protobuf nested message example.

This script shows:
1. Creating nested protobuf messages
2. Working with repeated message fields
3. Writing protobuf data to a binary file
4. Reading protobuf data from a binary file
"""

from pathlib import Path

# Generated protobuf Python module
# Generated using:
# protoc --python_out=. complex.proto
import complex_pb2 as complex_pb


# Binary file path
PROTO_FILE_PATH = Path("complex.bin")


def create_complex_message() -> complex_pb.ComplexMessage:
    """Create and return complex protobuf message."""

    # Create protobuf object
    message = complex_pb.ComplexMessage()

    # ---------------------------------------------------------
    # Assign nested message fields
    # ---------------------------------------------------------

    # 'one_dummy' is a nested protobuf message
    message.one_dummy.id = 123
    message.one_dummy.name = "I am dummy message"

    # ---------------------------------------------------------
    # Add elements to repeated message field
    # ---------------------------------------------------------

    # First Way:
    # Create empty message using add()
    # and populate fields manually
    first_dummy = message.multiple_dummy.add()

    first_dummy.id = 345
    first_dummy.name = "I'm the first element in the array"

    # ---------------------------------------------------------

    # Second Way:
    # Add message directly using keyword arguments
    message.multiple_dummy.add(
        id=567,
        name="Abhishek",
    )

    # ---------------------------------------------------------

    # Third Way:
    # Create separate protobuf object
    # and extend repeated field
    third_dummy_message = complex_pb.DummyMessage()

    third_dummy_message.id = 999
    third_dummy_message.name = "I'm the last one"

    message.multiple_dummy.extend([third_dummy_message])

    return message


def serialize_message(
    message: complex_pb.ComplexMessage,
    file_path: Path,
) -> None:
    """Write protobuf message to binary file."""

    try:
        # Open file in binary write mode
        with file_path.open("wb") as binary_file:
            # Convert protobuf object into binary format
            serialized_data = message.SerializeToString()

            # Write binary data to file
            binary_file.write(serialized_data)

        print(f"[SUCCESS] Message serialized to: {file_path}")

    except OSError as error:
        print(f"[ERROR] Failed to write protobuf file: {error}")
        raise


def deserialize_message(
    file_path: Path,
) -> complex_pb.ComplexMessage:
    """Read protobuf message from binary file."""

    try:
        # Open file in binary read mode
        with file_path.open("rb") as binary_file:
            # Read binary content
            binary_data = binary_file.read()

        # Create empty protobuf object
        message = complex_pb.ComplexMessage()

        # Populate object using binary data
        message.ParseFromString(binary_data)

        print(f"[SUCCESS] Message deserialized from: {file_path}")

        return message

    except OSError as error:
        print(f"[ERROR] Failed to read protobuf file: {error}")
        raise

    except Exception as error:
        print(f"[ERROR] Failed to parse protobuf data: {error}")
        raise


def main() -> None:
    """Run complex protobuf example."""

    print("[INFO] Creating complex protobuf message...\n")

    # Create protobuf object
    complex_message = create_complex_message()

    # Print generated protobuf message
    print("[INFO] Generated Message:")
    print(complex_message)

    # Serialize protobuf object
    serialize_message(complex_message, PROTO_FILE_PATH)

    # Deserialize protobuf object
    complex_message_read = deserialize_message(PROTO_FILE_PATH)

    # Print deserialized protobuf object
    print("\n[INFO] Deserialized Message:")
    print(complex_message_read)


# Entry point
if __name__ == "__main__":
    main()

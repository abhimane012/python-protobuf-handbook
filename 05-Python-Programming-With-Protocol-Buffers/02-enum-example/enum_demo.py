"""
Simple protobuf enum example.

This script shows:
1. Creating a protobuf message with enum fields
2. Writing protobuf data to a binary file
3. Reading protobuf data from a binary file
"""

from pathlib import Path

# Generated protobuf Python module
# Generated using:
# protoc --python_out=. enum_example.proto
import enum_example_pb2 as enum_example_pb


# Binary file path
PROTO_FILE_PATH = Path("enums.bin")


def create_enum_message() -> enum_example_pb.EnumMessage:
    """Create and return protobuf enum message."""

    # Create protobuf object
    message = enum_example_pb.EnumMessage()

    # Assign scalar field
    message.id = 123

    # Assign enum field
    #
    # MONDAY is defined inside enum_example.proto
    message.day_of_the_week = enum_example_pb.MONDAY

    return message


def serialize_message(
    message: enum_example_pb.EnumMessage,
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
) -> enum_example_pb.EnumMessage:
    """Read protobuf message from binary file."""

    try:
        # Open file in binary read mode
        with file_path.open("rb") as binary_file:

            # Read binary content
            binary_data = binary_file.read()

        # Create empty protobuf object
        message = enum_example_pb.EnumMessage()

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
    """Run protobuf enum example."""

    print("[INFO] Creating protobuf enum message...\n")

    # Create protobuf object
    enum_message = create_enum_message()

    # Print generated protobuf message
    print("[INFO] Generated Message:")
    print(enum_message)

    # Serialize protobuf object
    serialize_message(enum_message, PROTO_FILE_PATH)

    # Deserialize protobuf object
    enum_message_read = deserialize_message(PROTO_FILE_PATH)

    # Print deserialized protobuf object
    print("\n[INFO] Deserialized Message:")
    print(enum_message_read)


# Entry point
if __name__ == "__main__":
    main()
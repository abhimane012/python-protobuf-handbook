"""
Simple Protocol Buffers example.

This script shows:
1. Creating a protobuf message
2. Writing protobuf data to a binary file
3. Reading protobuf data from a binary file
"""

from pathlib import Path

# Generated protobuf Python module
# Generated using:
# protoc --python_out=. simple.proto
import simple_pb2 as simple_pb


# Binary file path
PROTO_FILE_PATH = Path("simple.bin")


def create_simple_message() -> simple_pb.SimpleMessage:
    """Create and return a protobuf message."""

    # Create protobuf object
    message = simple_pb.SimpleMessage()

    # Assign values to fields
    message.id = 10
    message.is_simple = True
    message.name = "Abhishek"

    # Add values to repeated field
    message.sample_list.extend([1, 2, 3])

    return message


def serialize_message(
    message: simple_pb.SimpleMessage,
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


def deserialize_message(file_path: Path) -> simple_pb.SimpleMessage:
    """Read protobuf message from binary file."""

    try:
        # Open file in binary read mode
        with file_path.open("rb") as binary_file:
            # Read binary content
            binary_data = binary_file.read()

        # Create empty protobuf object
        message = simple_pb.SimpleMessage()

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
    """Run protobuf serialization example."""

    print("[INFO] Creating protobuf message...\n")

    # Create protobuf object
    simple_message = create_simple_message()

    # Print repeated field details
    print(
        "[INFO] sample_list:",
        list(simple_message.sample_list),
    )

    print(
        "[INFO] sample_list type:",
        type(simple_message.sample_list),
    )

    # Print protobuf message
    print("\n[INFO] Generated Message:")
    print(simple_message)

    # Serialize protobuf object
    serialize_message(simple_message, PROTO_FILE_PATH)

    # Deserialize protobuf object
    deserialized_message = deserialize_message(PROTO_FILE_PATH)

    # Print deserialized object
    print("\n[INFO] Deserialized Message:")
    print(deserialized_message)


# Entry point
if __name__ == "__main__":
    main()

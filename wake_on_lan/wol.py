from typing import List, Union
import socket


class WakeOnLAN:
    DEFAULT_PORT: int = 9
    DEFAULT_BROADCAST_IP: str = "255.255.255.255"

    @staticmethod
    def validate_mac(mac_adress: str) -> str:
        """Validate if given MACs are in correct format

        Args:
            mac_adress (str): MAC to validate

        Raises:
            ValueError: If MAC has invalid format

        Returns:
            str: Validated MAC
        """

        if len(mac_adress) == 17:
            separation_mark = mac_adress[2]
            mac_adress = mac_adress.replace(separation_mark, "")

        elif len(mac_adress) != 12:
            raise ValueError("Invalid MAC address format")

        return mac_adress

    @staticmethod
    def create_magic_macket(mac_adress: str) -> bytes:
        """Will create magic packet for wol

        Args:
            mac_adress (str): MAC adress you want to create wol packet from

        Returns:
            bytes: magic packet
        """
        if not WakeOnLAN.validate_mac(mac_adress):
            return None

        return bytes.fromhex(6 * "FF" + WakeOnLAN.validate_mac(mac_adress) * 16)

    @staticmethod
    def send_magic_packet(
        macs: Union[str, List[str]],
        broadcast_ip: str = DEFAULT_BROADCAST_IP,
        port: int = DEFAULT_PORT,
    ) -> None:
        """Will send magic packet to given MAC address

        Args:
            macs (Union[str, List[str]]): string or list of strings of MACs
            broadcast_ip (str, optional): IP of the broadcast. Defaults to DEFAULT_BROADCAST_IP.
            port (int, optional): port of wol. Defaults to DEFAULT_PORT.

        Returns:
            None: None
        """

        if type(macs) == str:
            macs = [macs]
        magic_packets = [WakeOnLAN.create_magic_macket(mac) for mac in macs]

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.connect((broadcast_ip, port))

            for packet in magic_packets:
                sock.send(packet)

        return None

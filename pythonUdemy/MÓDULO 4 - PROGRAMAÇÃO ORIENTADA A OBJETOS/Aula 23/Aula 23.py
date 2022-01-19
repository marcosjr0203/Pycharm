"""
MÓDULO 4
AULA 23
PROJETO
CALCULANDO REDES IPV4
"""
import re


class CalcIPv4:
    """
    Faz o cálculo de redes IPv4

    Modo de uso 1:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefixo=10)

    Modo de uso 2:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.0')
    """

    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        if mascara is None and prefixo is None:
            raise ValueError('Precisa enviar máscara ou prefixo')

        if mascara and prefixo:
            raise ValueError('Precisa enviar máscara ou prefixo, não ambos.')

        self._set_broadcast()
        self._set_rede()

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self._get_numero_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        if self._prefixo is None:
            return

        return self._prefixo

    @ip.setter
    def ip(self, valor):
        if not self._valida_ip(valor):
            raise ValueError('IP inválido.')

        self._ip = valor
        self._ip_bin = self._ip_to_bin(valor)

    @mascara.setter
    def mascara(self, valor):
        if not valor:
            return

        if not self._valida_ip(valor):
            raise ValueError('Máscara inválida.')

        self._mascara = valor
        self._mascara_bin = self._ip_to_bin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        if valor is None:
            return

        try:
            valor = int(valor)
        except:
            raise ValueError('Prefixo precisa ser um inteiro.')

        if valor > 32 or valor < 0:
            raise TypeError('Prefixo precisa ter 32Bits.')

        self._prefixo = valor
        self._mascara_bin = (valor * '1').ljust(32, '0')

        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.')
        blocos_bin = [bin(int(bloco))[2:].zfill(8) for bloco in blocos]
        blocos_bin_str = ''.join(blocos_bin)
        qtd_bits = len(blocos_bin_str)

        if qtd_bits > 32:
            raise ValueError('IP ou máscara tem mais que 32 bits.')

        return blocos_bin_str

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _set_broadcast(self):
        host_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (host_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_numero_ips(self):
        return 2 ** (32 - self.prefixo)


def main():
    """ Exemplos de Uso """

    # Com prefixo
    calc_ipv4_1 = CalcIPv4(ip='192.168.0.128', prefixo=30)

    print(f'IP: {calc_ipv4_1.ip}')
    print(f'Máscara: {calc_ipv4_1.mascara}')
    print(f'Rede: {calc_ipv4_1.rede}')
    print(f'Broadcast: {calc_ipv4_1.broadcast}')
    print(f'Prefixo: {calc_ipv4_1.prefixo}')
    print(f'Número de IPs da rede: {calc_ipv4_1.numero_ips}')

    print('#' * 80)

    # Com máscara
    calc_ipv4_2 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.192')

    print(f'IP: {calc_ipv4_2.ip}')
    print(f'Máscara: {calc_ipv4_2.mascara}')
    print(f'Rede: {calc_ipv4_2.rede}')
    print(f'Broadcast: {calc_ipv4_2.broadcast}')
    print(f'Prefixo: {calc_ipv4_2.prefixo}')
    print(f'Número de IPs da rede: {calc_ipv4_2.numero_ips}')


if __name__ == '__main__':
    main()

from decimal import Decimal

import ipfshttpclient
from web3 import Account, Web3
from web3.eth import TxReceipt
from web3.middleware import geth_poa_middleware

# POLYGON_TESTNET = "https://rpc-mumbai.maticvigil.com/"
# EVMOS_TESTNET = "https://eth.bd.evmos.dev:8545"

class Book():
    def __init__(self, network_address: str):
        self.web3 = Web3(Web3.HTTPProvider(network_address))
        self.BOOK_ABI = open("book.abi", "r").read()
        self.BOOK_BYTECODE = open("book.bin", "r").read()
    
    def load_data(self):
        """load neccessary data to work with the object"""
        Account.enable_unaudited_hdwallet_features()
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def get_author(self, contract_address: str) -> str:
        """return book author"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.Author().call()

    def get_title(self, contract_address: str) -> str:
        """return book title"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.Title().call()

    def get_book_license(self, contract_address: str) -> str:
        """return book book_license"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.License().call()

    def get_chapters_count(self, contract_address: str) -> int:
        """return book chapters count"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.Chapters().call()

    def get_chapter_name(self, contract_address: str, chapterid: int) -> str:
        """return book chapter name"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.Book(chapterid).call()[1]

    def get_chapter_content(self, contract_address: str, chapterid: int) -> str:
        """return book chapter content"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.Book(chapterid).call()[3]

    def get_chapter_status(self, contract_address: str, chapterid: int) -> bool:
        """return book chapter status"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return book.functions.Book(chapterid).call()[0]

    def deposit_ether_to_contract(self, contract_address: str, amount: float, mnemonic: str) -> bool:
        """Deposit ether to the contract"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        tx_hash = {
        'from': addr,
        'to': self.web3.toChecksumAddress(contract_address),
        'value': self.web3.toWei(amount, 'ether'),
        'nonce': self.web3.eth.get_transaction_count(addr),
        'gas': 2000000,
        'gasPrice': self.web3.toWei('200', 'gwei'),
        'chainId': self.web3.eth.chain_id
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx_hash, private_key=key)
        send_it = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_it)

    def new_chapter(self, contract_address: str, chapter_id: int, chapter_name: str, chapter_content: str, mnemonic: str) -> TxReceipt:
        """create new chapter"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        txn = book.functions.addchapter(chapter_id, chapter_name, chapter_content).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr)
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)

    def remove_chapter(self, contract_address: str, chapterid: int, mnemonic: str) -> TxReceipt:
        """remove chapter"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        txn = book.functions.removechapter(chapterid).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr)
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)

    def new_book(self, title: str, book_license: str, mnemonic: str) -> TxReceipt:
        """create new book"""
        book = self.web3.eth.contract(abi=self.BOOK_ABI, bytecode=self.BOOK_BYTECODE)
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        txn = book.constructor(title, book_license).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)

    def get_book_balance(self, contract_address: str) -> Decimal:
        """return book balance"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return self.web3.fromWei(book.functions.balanceof().call(), 'ether')

    def get_all_time_value(self, contract_address: str) -> Decimal:
        """return book all time value"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return self.web3.fromWei(book.functions.AllTimeValue().call(), 'ether')

    def transfer_ether_from_book_contract(self, contract_address: str, mnemonic: str, amount: int, to: str) -> TxReceipt:
        """transfer ether from contract"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        txn = book.functions.transfer(self.web3.toChecksumAddress(to), self.web3.toWei(amount, 'gwei')).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)

class Library():
    def __init__(self, network_address: str):
        self.web3 = Web3(Web3.HTTPProvider(network_address))
        self.LIBRARY_ABI = open("library.abi", "r").read()
        self.LIBRARY_BYTECODE = open("library.bin", "r").read()
    
    def load_data(self):
        """load neccessary data to work with the object"""
        Account.enable_unaudited_hdwallet_features()
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def get_library_name(self, contract_address: str) -> str:
        """return library name"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.LibraryName().call()
    
    def get_librarian(self, contract_address: str) -> str:
        """return library librarian"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.Librarian().call()
    
    def get_book_count(self, contract_address: str) -> int:
        """return book count"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.BookCount().call()
    
    def get_all_time_value(self, contract_address: str) -> Decimal:
        """return library all time value"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return self.web3.fromWei(library.functions.AllTimeValue().call(), 'ether')
    
    def get_quote(self, contract_address: str) -> str:
        """return library quote"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.Quote().call()
    
    def get_book_title(self, contract_address: str, book_id: int) -> str:
        """return book title"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.Library(book_id).call()[3]
    
    def get_book_author(self, contract_address: str, book_id: int) -> str:
        """return book author"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.Library(book_id).call()[2]
    
    def get_book_address(self, contract_address: str, book_id: int) -> str:
        """return book address"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.Library(book_id).call()[1]
    
    def get_book_status(self, contract_address: str, book_id: int) -> bool:
        """return book status"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return library.functions.Library(book_id).call()[0]
    
    def deposit_ether_to_contract(self, contract_address: str, amount: float, mnemonic: str) -> bool:
        """Deposit ether to the contract"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        tx_hash = {
        'from': addr,
        'to': self.web3.toChecksumAddress(contract_address),
        'value': self.web3.toWei(amount, 'ether'),
        'nonce': self.web3.eth.get_transaction_count(addr),
        'gas': 2000000,
        'gasPrice': self.web3.toWei('20', 'gwei'),
        'chainId': self.web3.eth.chain_id
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx_hash, private_key=key)
        send_it = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_it)

    def new_library(self, name: str, mnemonic: str) -> TxReceipt:
        """create new library"""
        library = self.web3.eth.contract(abi=self.LIBRARY_ABI, bytecode=self.LIBRARY_BYTECODE)
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        txn = library.constructor(name).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)
    
    def add_book(self, contract_address: str, book_id: int, book_address: str, mnemonic: str) -> TxReceipt:
        """add book to library"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        txn = library.functions.addbook(book_id, book_address).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)
    
    def remove_book(self, contract_address: str, book_id: int, mnemonic: str) -> TxReceipt:
        """remove book from library"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        txn = library.functions.removebook(book_id).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)
    
    def transfer_position(self, contract_address: str, new_librarian: str, mnemonic: str) -> TxReceipt:
        """transfer librarian position"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        txn = library.functions.transferposition(new_librarian).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)
    
    def transfer_ether_from_library_contract(self, contract_address: str, to: str, amount: int, mnemonic: str) -> TxReceipt:
        """transfer ether from library contract"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        txn = library.functions.transfer(self.web3.toChecksumAddress(to), self.web3.toWei(amount, 'gwei')).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)
    
    def get_library_balance(self, contract_address: str) -> int:
        """get library balance"""
        library = self.web3.eth.contract(address=contract_address, abi=self.LIBRARY_ABI)
        return self.web3.toWei(library.functions.balanceof().call(), 'ether')

class BookIPFS():
    def __init__(self, network_address: str):
        self.web3 = Web3(Web3.HTTPProvider(network_address))
        self.BOOKIPFS_ABI = open("book_ipfs.abi", "r").read()
        self.BOOKIPFS_BYTECODE = open("book_ipfs.bin", "r").read()

    def load_data(self):
        """load neccessary data to work with the object"""
        Account.enable_unaudited_hdwallet_features()
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def get_author(self, contract_address: str) -> str:
        """return book author"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        return book.functions.Author().call()

    def get_title(self, contract_address: str) -> str:
        """return book title"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        return book.functions.Title().call()
    
    def get_book_format(self, contract_address: str) -> str:
        """return book format as deployed to ipfs, used to build the book from the hash"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        return book.functions.BookFormat().call()

    def get_book_license(self, contract_address: str) -> str:
        """return book book_license"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        return book.functions.License().call()
    
    def get_ipfs_hash(self, contract_address: str) -> str:
        """return book ipfs hash"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        return book.functions.IpfsHash().call()
    
    def deposit_ether_to_contract(self, contract_address: str, amount: float, mnemonic: str) -> bool:
        """Deposit ether to the contract"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        tx_hash = {
        'from': addr,
        'to': self.web3.toChecksumAddress(contract_address),
        'value': self.web3.toWei(amount, 'ether'),
        'nonce': self.web3.eth.get_transaction_count(addr),
        'gas': 2000000,
        'gasPrice': self.web3.toWei('20', 'gwei'),
        'chainId': self.web3.eth.chain_id
        }
        signed_tx = self.web3.eth.account.sign_transaction(tx_hash, private_key=key)
        send_it = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_it)
    
    def new_ipfs_book(self, title: str, book_license: str, book_path: str, book_format: str, ipfs_client: ipfshttpclient, mnemonic: str) -> TxReceipt:
        """create new ipfs book this is also upload the book to ipfs"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        ipfs_hash = self.upload_to_ipfs(book_path, ipfs_client)
        book = self.web3.eth.contract(abi=self.BOOKIPFS_ABI, bytecode=self.BOOKIPFS_BYTECODE)
        txn = book.constructor(title, book_license, ipfs_hash, book_format).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)
    
    def resolve_book_from_ipfs(self, contract_address: str, ipfs_client: ipfshttpclient) -> bool:
        """return the book from ipfs"""
        name = self.get_title(contract_address)
        ipfs_hash = self.get_ipfs_hash(contract_address)
        book_format = self.get_book_format(contract_address)
        resolve_book = open(f"{name}.{book_format}", "wb")
        resolve_book.write(ipfs_client.cat(ipfs_hash))
        return True
    
    def upload_to_ipfs(self, book_path: str, ipfs_client: ipfshttpclient) -> str:
        """upload book to ipfs"""
        book_hash = ipfs_client.add(book_path)
        return book_hash['Hash']

    def get_ipfs_book_balance(self, contract_address: str) -> Decimal:
        """return book balance"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOK_ABI)
        return self.web3.fromWei(book.functions.balanceof().call(), 'ether')

    def get_all_time_value(self, contract_address: str) -> Decimal:
        """return book all time value"""
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        return self.web3.fromWei(book.functions.AllTimeValue().call(), 'ether')

    def transfer_ether_from_book_contract(self, contract_address: str, mnemonic: str, amount: int, to: str) -> TxReceipt:
        """transfer ether from contract"""
        acc = self.web3.eth.account.from_mnemonic(mnemonic)
        addr = acc.address
        key = acc.key
        book = self.web3.eth.contract(address=contract_address, abi=self.BOOKIPFS_ABI)
        txn = book.functions.transfer(self.web3.toChecksumAddress(to), self.web3.toWei(amount, 'gwei')).buildTransaction({
            'from': addr,
            'nonce': self.web3.eth.get_transaction_count(addr),
            'chainId': self.web3.eth.chainId
        })
        stxn = self.web3.eth.account.sign_transaction(txn, private_key=key)
        send_stxn = self.web3.eth.send_raw_transaction(stxn.rawTransaction)
        return self.web3.eth.wait_for_transaction_receipt(send_stxn)


# b = Book()
# print(b.get_author("0x647a57bA83832DC6d69Ac600155511eAC3024ff1"))

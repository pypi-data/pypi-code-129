from decimal import Decimal

import ipfshttpclient
from web3 import Account, Web3
from web3.eth import TxReceipt
from web3.middleware import geth_poa_middleware

# load binaries
BOOK_ABI = """[{"name": "AddedChapter", "inputs": [{"name": "Author", "type": "address", "indexed": true}, {"name": "Chapter_id", "type": "uint256", "indexed": true}, {"name": "Name", "type": "string", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "RemovedChapter", "inputs": [{"name": "Author", "type": "address", "indexed": true}, {"name": "Chapter_id", "type": "uint256", "indexed": true}, {"name": "Name", "type": "string", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Deposit", "inputs": [{"name": "sender", "type": "address", "indexed": true}, {"name": "value", "type": "uint256", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Transfer", "inputs": [{"name": "sender", "type": "address", "indexed": true}, {"name": "receiver", "type": "address", "indexed": true}, {"name": "value", "type": "uint256", "indexed": false}], "anonymous": false, "type": "event"}, {"stateMutability": "nonpayable", "type": "constructor", "inputs": [{"name": "_title", "type": "string"}, {"name": "_license", "type": "string"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "addchapter", "inputs": [{"name": "_chapter", "type": "uint256"}, {"name": "_name", "type": "string"}, {"name": "_content", "type": "string"}], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "nonpayable", "type": "function", "name": "removechapter", "inputs": [{"name": "_chapter", "type": "uint256"}], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "nonpayable", "type": "function", "name": "transfer", "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "outputs": []}, {"stateMutability": "view", "type": "function", "name": "balanceof", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "payable", "type": "fallback"}, {"stateMutability": "view", "type": "function", "name": "Author", "inputs": [], "outputs": [{"name": "", "type": "address"}]}, {"stateMutability": "view", "type": "function", "name": "Title", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "License", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "Chapters", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "Book", "inputs": [{"name": "arg0", "type": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "ispresent", "type": "bool"}, {"name": "name", "type": "string"}, {"name": "chapterid", "type": "uint256"}, {"name": "content", "type": "string"}]}]}, {"stateMutability": "view", "type": "function", "name": "AllTimeValue", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}]"""
BOOK_BIN = "0x6020610a96600039600051610100602082610a960160003960005111610a9157602081610a960160003960005180604052602082018181610a96016060395050506020610ab6600039600051610100602082610a960160003960005111610a9157602081610a96016000396000518061016052602082018181610a96016101803950505034610a91573360005560405180600155600081601f0160051c60088111610a915780156100c457905b8060051b6060015181600201556001018181186100ac575b5050506101605180600a55600081601f0160051c60088111610a9157801561010157905b8060051b610180015181600b01556001018181186100e8575b50505061097a6101166100003961097a610000f36003361161000c57610928565b60003560e01c63278a384e811861031d5760a4361061096a5760243560040161010081351161096a57803580604052602082018181606037505050604435600401620f424081351161096a5780358061016052602082018181610180375050503461096a57600054331815610110576024620f43c0527f596f7520617265206e6f7420617574686f72697a6564203a2920746f20646f20620f43e0527f7468697300000000000000000000000000000000000000000000000000000000620f440052620f43c050620f43c05180620f43e001601f826000031636823750506308c379a0620f4380526020620f43a052601f19601f620f43c0510116604401620f439cfd5b601460043560205260005260406000205415610195576016620f43c0527f4368617074657220616c72656164792065786973747300000000000000000000620f43e052620f43c050620f43c05180620f43e001601f826000031636823750506308c379a0620f4380526020620f43a052601f19601f620f43c0510116604401620f439cfd5b6001620f43c05260405180620f43e05280620f440082606060045afa5050600435620f4500526101605180620f45205280620f45408261018060045afa50506013546001810181811061096a57905060135560146004356020526000526040600020620f43c0518155620f43e05180600183015560016001830101600082601f0160051c6008811161096a57801561024257905b8060051b620f4400015181840155600101818118610229575b50505050620f450051600a820155620f45205180600b8301556001600b830101600082601f0160051c617a12811161096a57801561029557905b8060051b620f454001518184015560010181811861027c575b5050505050600435337fcfa7c47ae096a3e0d7a994ea1a1b67b11b4d47344943eff18abe0db56906b58e602080621e87805280621e87800160405180825260208201818183606060045afa5050508051806020830101601f82600003163682375050601f19601f82516020010116905081019050621e8780a36001621e8780526020621e8780f35b633eacc66e81186105d2576024361861096a573461096a576000543318156103c05760246040527f596f7520617265206e6f7420617574686f72697a6564203a2920746f20646f206060527f746869730000000000000000000000000000000000000000000000000000000060805260405060405180606001601f826000031636823750506308c379a06000526020602052601f19601f6040510116604401601cfd5b6001601460043560205260005260406000205418156104365760146040527f4368617074657220646f65736e7420657869737400000000000000000000000060605260405060405180606001601f826000031636823750506308c379a06000526020602052601f19601f6040510116604401601cfd5b60146004356020526000526040600020546040526014600435602052600052604060002060018101905080548060605260018201600082601f0160051c6008811161096a57801561049a57905b808301548160051b60800152600101818118610483575b505050505060146004356020526000526040600020600a81019050546101805260146004356020526000526040600020600b810190508054806101a05260018201600082601f0160051c617a12811161096a57801561050d57905b808301548160051b6101c001526001018181186104f5575b50505050506014600435602052600052604060002060008155600060018201556000600a8201556000600b820155506013546001810381811161096a579050601355600435337f02f4d88f3a80b9f93023b157415cd145feb059067ddb801c358385a2a9ca8b04602080620f44005280620f44000160605180825260208201818183608060045afa5050508051806020830101601f82600003163682375050601f19601f82516020010116905081019050620f4400a36001620f4400526020620f4400f35b63a9059cbb8118610649576044361861096a576004358060a01c61096a576040523461096a57600054331861096a5760006000600060006024356040516000f11561096a57604051337fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60243560605260206060a3005b632980a5d3811861066b576004361861096a573461096a574760405260206040f35b6320b2af52811861068f576004361861096a573461096a5760005460405260206040f35b63b87f04048118610719576004361861096a573461096a576020806040528060400160015480825260208201600082601f0160051c6008811161096a5780156106eb57905b80600201548160051b8401526001018181186106d4575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63cf21316381186107a3576004361861096a573461096a5760208060405280604001600a5480825260208201600082601f0160051c6008811161096a57801561077557905b80600b01548160051b84015260010181811861075e575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63774cd99381186107c7576004361861096a573461096a5760135460405260206040f35b63022481ff8118610902576024361861096a573461096a5760208060405260146004356020526000526040600020816040016080825482528060208301526001830181830181548082526001830160208301600083601f0160051c6008811161096a57801561084857905b808401548160051b840152600101818118610832575b50505050508051806020830101601f82600003163682375050601f19601f825160200101169050905081019050600a8301546040830152806060830152600b830181830181548082526001830160208301600083601f0160051c617a12811161096a5780156108c957905b808401548160051b8401526001018181186108b3575b50505050508051806020830101601f82600003163682375050601f19601f82516020010116905090508101905090509050810190506040f35b63fd2d205e8118610926576004361861096a573461096a5760155460405260206040f35b505b6015543480820182811061096a5790509050601555337fe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c3460405260206040a2005b600080fda165767970657283000304005b600080fd"

BOOK_IPFS_ABI = """[{"name": "Deposit", "inputs": [{"name": "sender", "type": "address", "indexed": true}, {"name": "value", "type": "uint256", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Transfer", "inputs": [{"name": "sender", "type": "address", "indexed": true}, {"name": "receiver", "type": "address", "indexed": true}, {"name": "value", "type": "uint256", "indexed": false}], "anonymous": false, "type": "event"}, {"stateMutability": "nonpayable", "type": "constructor", "inputs": [{"name": "_title", "type": "string"}, {"name": "_license", "type": "string"}, {"name": "_ipfshash", "type": "string"}, {"name": "_bookformat", "type": "string"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "transfer", "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "outputs": []}, {"stateMutability": "view", "type": "function", "name": "balanceof", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "payable", "type": "fallback"}, {"stateMutability": "view", "type": "function", "name": "Author", "inputs": [], "outputs": [{"name": "", "type": "address"}]}, {"stateMutability": "view", "type": "function", "name": "Title", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "License", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "BookFormat", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "IpfsHash", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "AllTimeValue", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}]"""
BOOK_IPFS_BIN = "0x602061058a60003960005161010060208261058a01600039600051116105855760208161058a016000396000518060405260208201818161058a0160603950505060206105aa60003960005161010060208261058a01600039600051116105855760208161058a01600039600051806101605260208201818161058a016101803950505060206105ca60003960005161010060208261058a01600039600051116105855760208161058a01600039600051806102805260208201818161058a016102a03950505060206105ea600039600051608060208261058a01600039600051116105855760208161058a01600039600051806103a05260208201818161058a016103c03950505034610585573360005560405180600155600081601f0160051c6008811161058557801561014957905b8060051b606001518160020155600101818118610131575b5050506101605180600a55600081601f0160051c6008811161058557801561018657905b8060051b610180015181600b015560010181811861016d575b5050506102805180601855600081601f0160051c600881116105855780156101c357905b8060051b6102a0015181601901556001018181186101aa575b5050506103a05180601355600081601f0160051c6004811161058557801561020057905b8060051b6103c0015181601401556001018181186101e7575b50505061036f6102156100d13961036f6100d1f36003361161000c5761031d565b60003560e01c63a9059cbb8118610089576044361861035f576004358060a01c61035f576040523461035f57600054331861035f5760006000600060006024356040516000f11561035f57604051337fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60243560605260206060a3005b632980a5d381186100ab576004361861035f573461035f574760405260206040f35b6320b2af5281186100cf576004361861035f573461035f5760005460405260206040f35b63b87f04048118610159576004361861035f573461035f576020806040528060400160015480825260208201600082601f0160051c6008811161035f57801561012b57905b80600201548160051b840152600101818118610114575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63cf21316381186101e3576004361861035f573461035f5760208060405280604001600a5480825260208201600082601f0160051c6008811161035f5780156101b557905b80600b01548160051b84015260010181811861019e575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63ea0859ec811861026d576004361861035f573461035f576020806040528060400160135480825260208201600082601f0160051c6004811161035f57801561023f57905b80601401548160051b840152600101818118610228575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b638bf421ee81186102f7576004361861035f573461035f576020806040528060400160185480825260208201600082601f0160051c6008811161035f5780156102c957905b80601901548160051b8401526001018181186102b2575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63fd2d205e811861031b576004361861035f573461035f5760215460405260206040f35b505b6021543480820182811061035f5790509050602155337fe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c3460405260206040a2005b600080fda165767970657283000304005b600080fd"

LIBRARY_ABI = """[{"name": "AddBook", "inputs": [{"name": "librarian", "type": "address", "indexed": true}, {"name": "bookaddr", "type": "address", "indexed": true}, {"name": "author", "type": "address", "indexed": true}, {"name": "title", "type": "string", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "RemoveBook", "inputs": [{"name": "librarian", "type": "address", "indexed": true}, {"name": "bookaddr", "type": "address", "indexed": true}, {"name": "author", "type": "address", "indexed": true}, {"name": "title", "type": "string", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Deposit", "inputs": [{"name": "sender", "type": "address", "indexed": true}, {"name": "value", "type": "uint256", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Transfer", "inputs": [{"name": "sender", "type": "address", "indexed": true}, {"name": "receiver", "type": "address", "indexed": true}, {"name": "value", "type": "uint256", "indexed": false}], "anonymous": false, "type": "event"}, {"stateMutability": "nonpayable", "type": "constructor", "inputs": [{"name": "_library_name", "type": "string"}], "outputs": []}, {"stateMutability": "payable", "type": "fallback"}, {"stateMutability": "nonpayable", "type": "function", "name": "addbook", "inputs": [{"name": "_id", "type": "uint256"}, {"name": "_bookaddr", "type": "address"}], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "nonpayable", "type": "function", "name": "removebook", "inputs": [{"name": "_id", "type": "uint256"}], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "nonpayable", "type": "function", "name": "transferposition", "inputs": [{"name": "_new_librarian", "type": "address"}], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "nonpayable", "type": "function", "name": "transfer", "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "outputs": []}, {"stateMutability": "view", "type": "function", "name": "balanceof", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "LibraryName", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "Librarian", "inputs": [], "outputs": [{"name": "", "type": "address"}]}, {"stateMutability": "view", "type": "function", "name": "BookCount", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "AllTimeValue", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "Quote", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "Library", "inputs": [{"name": "arg0", "type": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "ispresent", "type": "bool"}, {"name": "bookaddr", "type": "address"}, {"name": "author", "type": "address"}, {"name": "title", "type": "string"}]}]}]"""
LIBRARY_BIN = "0x6020610ca9600039600051610100602082610ca90160003960005111610ca457602081610ca90160003960005180604052602082018181610ca90160603950505034610ca45760405180600055600081601f0160051c60088111610ca457801561007d57905b8060051b606001518160010155600101818118610065575b5050503360095561010d610160527f27486f77206461726520796f7520616e64207468652072657374206f6620796f610180527f75722062617262617269616e7320736574206669726520746f206d79206c69626101a0527f726172793f200a20506c617920636f6e717565726f7220616c6c20796f7520776101c0527f616e742c204d6967687479204361657361722120526170652c206d75726465726101e0527f2c2070696c6c6167652074686f7573616e64732c206576656e206d696c6c696f610200527f6e73206f662068756d616e206265696e677321200a20427574206e6569746865610220527f7220796f75206e6f7220616e79206f746865722062617262617269616e206861610240527f732074686520726967687420746f2064657374726f79206f6e652068756d616e610260527f2074686f7567687421270a200a0000000000000000000000000000000000000061028052610160805180600c5560208201600082601f0160051c60098111610ca457801561021557905b8060051b83015181600d01556001018181186101fe575b5050505050610a7761022c61000039610a77610000f36003361161000c57610967565b60003560e01c63a795facc81186102c65760443618610a67576024358060a01c610a67576102e05234610a67576009543318156100ce576027610300527f6f6e6c7920746865206c696272617269616e2063616e2063616c6c2074686973610320527f206d6574686f64000000000000000000000000000000000000000000000000006103405261030050610300518061032001601f826000031636823750506308c379a06102c05260206102e052601f19601f6103005101166044016102dcfd5b602d6004356020526000526040600020541561014a576013610300527f696420697320616c72656164792074616b656e000000000000000000000000006103205261030050610300518061032001601f826000031636823750506308c379a06102c05260206102e052601f19601f6103005101166044016102dcfd5b6102e05160405261015c610320610a22565b61032051610300526102e0516040526101766104406109a9565b610440805180610320526020820181610340838360045afa505050506001610440526102e05161046052610300516104805261032051806104a052806104c08261034060045afa5050602d60043560205260005260406000206104405181556104605160018201556104805160028201556104a05180600383015560016003830101600082601f0160051c60088111610a6757801561022957905b8060051b6104c0015181840155600101818118610211575b5050505050600a5460018101818110610a67579050600a55610300516102e051337fd0ccea6680790433af43978f9ba0ee2743697b2119e30f4b7d272174a63c53ad6020806105c052806105c001610320518082526020820181818361034060045afa5050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506105c0a460016105c05260206105c0f35b63f131dd45811861053a5760243618610a675734610a67576009543318156103695760276040527f6f6e6c7920746865206c696272617269616e2063616e2063616c6c20746869736060527f206d6574686f640000000000000000000000000000000000000000000000000060805260405060405180606001601f826000031636823750506308c379a06000526020602052601f19601f6040510116604401601cfd5b6001602d60043560205260005260406000205418156103df5760156040527f7468657265206973206e6f7468696e672068657265000000000000000000000060605260405060405180606001601f826000031636823750506308c379a06000526020602052601f19601f6040510116604401601cfd5b602d600435602052600052604060002054604052602d600435602052600052604060002060018101905054606052602d600435602052600052604060002060028101905054608052602d600435602052600052604060002060038101905080548060a05260018201600082601f0160051c60088111610a6757801561047757905b808301548160051b60c00152600101818118610460575b5050505050602d60043560205260005260406000206000815560006001820155600060028201556000600382015550600a5460018103818111610a67579050600a55608051606051337f5f65519d08b3f324f25e0a718dd68aa6319d9c1045f8bcd2e6587021a61cf08c6020806101c052806101c00160a0518082526020820181818360c060045afa5050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506101c0a460016101c05260206101c0f35b63733c3c3d81186105fc5760243618610a67576004358060a01c610a675760405234610a67576009543318156105eb5760276060527f6f6e6c7920746865206c696272617269616e2063616e2063616c6c20746869736080527f206d6574686f640000000000000000000000000000000000000000000000000060a05260605060605180608001601f826000031636823750506308c379a06020526020604052601f19601f6060510116604401603cfd5b604051600955600160605260206060f35b63a9059cbb81186106f55760443618610a67576004358060a01c610a675760405234610a67576009543318156106ad5760276060527f6f6e6c7920746865206c696272617269616e2063616e2063616c6c20746869736080527f206d6574686f640000000000000000000000000000000000000000000000000060a05260605060605180608001601f826000031636823750506308c379a06020526020604052601f19601f6060510116604401603cfd5b60006000600060006024356040516000f115610a6757604051337fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef60243560605260206060a3005b632980a5d381186107175760043618610a675734610a67574760405260206040f35b630ae0c81681186107a15760043618610a675734610a67576020806040528060400160005480825260208201600082601f0160051c60088111610a6757801561077357905b80600101548160051b84015260010181811861075c575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63756fe37481186107c55760043618610a675734610a675760095460405260206040f35b6329c37f9181186107e95760043618610a675734610a6757600a5460405260206040f35b63fd2d205e811861080d5760043618610a675734610a6757600b5460405260206040f35b63335b3bef81186108975760043618610a675734610a675760208060405280604001600c5480825260208201600082601f0160051c60208111610a6757801561086957905b80600d01548160051b840152600101818118610852575b505050508051806020830101601f82600003163682375050601f19601f825160200101169050810190506040f35b63e083e0df81186109655760243618610a675734610a6757602080604052602d60043560205260005260406000208160400160808254825260018301546020830152600283015460408301528060608301526003830181830181548082526001830160208301600083601f0160051c60088111610a6757801561092c57905b808401548160051b840152600101818118610916575b50505050508051806020830101601f82600003163682375050601f19601f82516020010116905090508101905090509050810190506040f35b505b600b5434808201828110610a675790509050600b55337fe1fffcc4923d04b559f4d29a8bfc6cda04eb5b0d3c460751c2402c5c5cc9109c3460405260206040a2005b60405163b87f040460605261014060606004607c845afa6109cf573d600060003e3d6000fd5b60403d10610a6757606051606001610100815111610a67578051806101c05260208201816101e0838360045afa505050506101c09050805180835260208201602084018281848460045afa505050505050565b6040516320b2af52606052602060606004607c845afa610a47573d600060003e3d6000fd5b60203d10610a67576060518060a01c610a675760a05260a0905051815250565b600080fda165767970657283000304005b600080fd"



# POLYGON_TESTNET = "https://rpc-mumbai.maticvigil.com/"
# EVMOS_TESTNET = "https://eth.bd.evmos.dev:8545"

class Book():
    def __init__(self, network_address: str):
        self.web3 = Web3(Web3.HTTPProvider(network_address))
        self.BOOK_ABI = BOOK_ABI
        self.BOOK_BYTECODE = BOOK_BIN
    
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
        self.LIBRARY_ABI = LIBRARY_ABI
        self.LIBRARY_BYTECODE = LIBRARY_BIN
    
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
        self.BOOKIPFS_ABI = BOOK_IPFS_ABI
        self.BOOKIPFS_BYTECODE = BOOK_IPFS_BIN

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

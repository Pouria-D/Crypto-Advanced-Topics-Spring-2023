# Cryptography Advanced Topics - Spring 2023

Welcome to the Cryptography Advanced Topics repository! This repository contains the projects completed during the **Cryptography Advanced Topics** course at Sharif University of Technology. The course explored various advanced topics in cryptographic systems, from blockchain analysis to securing VPN connections and lightweight cryptographic protocols.

## Project Overview

### 1. Blockchain Analysis: Uniswap Exchange

**Description**: The first project was a research-based analysis of the **Uniswap Exchange**. Uniswap is a decentralized exchange protocol on the Ethereum blockchain that allows users to swap ERC-20 tokens without intermediaries. This project provided an in-depth analysis of:
- The **automated market maker (AMM)** model utilized by Uniswap.
- The functioning of **liquidity pools** and their impact on token prices.
- The concept of **impermanent loss**, how it affects liquidity providers, and strategies to mitigate this risk.
- **Gas fees** and their implications on Uniswap's transactions.

**Key Insights**:
- Understanding the mechanism of **price discovery** in AMMs.
- Evaluating the **security features** and potential vulnerabilities in decentralized finance (DeFi).
- Assessing the scalability and cost implications of executing swaps on Ethereum.

**Note**: This project does not have an implemented codebase as it focused on theoretical and empirical analysis.

### 2. Securing OpenVPN: Enhancing Security Features

**Description**: The second project involved enhancing the security of **OpenVPN** to provide a more secure VPN connection. The focus was on implementing additional cryptographic measures to strengthen authentication and data integrity.

**Key Features**:
- **AES-GCM Encryption**: Integrated **AES-GCM** mode to ensure both encryption and integrity of the data transmitted through the VPN.
- **Multi-Factor Authentication (MFA)**: Added MFA support to enhance user authentication and protect against unauthorized access.
- **TLS Key Pinning**: Implemented **TLS key pinning** to prevent Man-in-the-Middle (MITM) attacks by ensuring the client only accepts a specific server certificate.
- **Certificate Revocation List (CRL)**: Added support for CRLs to ensure that compromised certificates are not used.

**Implementation Details**:
- The OpenVPN configuration was modified to use **AES-GCM** for data encryption and **TLS key pinning** for securing server-client communication.
- Additional scripts were added for managing **MFA** and **CRLs**.

**How to Run**:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pouria-D/Crypto-Advanced-Topics-Spring-2023.git
   cd Crypto-Advanced-Topics-Spring-2023/Project%202%20_%20Securing%20OVPN
   ```

2. **Install Dependencies**:
   Ensure **OpenVPN** and **OpenSSL** are installed on your system:
   ```bash
   sudo apt-get install openvpn openssl
   ```

3. **Configure OpenVPN**:
   - Update the configuration file (`server.conf` and `client.conf`) with the new settings for **AES-GCM** and **TLS key pinning**.
   - Use the provided script to generate certificates and keys.

4. **Run OpenVPN**:
   Start the server and client with the updated configurations to verify the enhanced security features.

### 3. Lightweight Cryptography: Integral Cryptanalysis of Customized SIMON

**Description**: The third project involved implementing **SIMON**, a lightweight block cipher developed by the NSA, and conducting an **integral cryptanalysis** of a customized version of the cipher. The aim was to explore the vulnerabilities of the modified SIMON algorithm and evaluate its resistance to cryptanalysis techniques.

**Key Components**:
- **Customized SIMON Implementation**: Implemented a modified version of SIMON with different block sizes and key lengths to evaluate the impact on security.
- **Integral Cryptanalysis**: Performed an integral attack on the customized version, focusing on identifying statistical biases that could lead to key recovery.

**Implementation Details**:
- The customized version of **SIMON** was implemented in Python, allowing flexibility in modifying parameters such as block size and key length.
- Developed scripts to execute the **integral cryptanalysis** attack, including key recovery for reduced-round versions of SIMON.
- Detailed analysis of the results was conducted to assess the effectiveness of the attack.

## Requirements
- **Python 3.8+** for SIMON cryptanalysis
- **OpenVPN** and **OpenSSL** for the VPN refinement project
- **Git** for cloning repositories

## Contact
Sorry The Reports are provided in Persian and currently i didn't prepare an english official report for them, For more details or questions, feel free to contact me at [pouria.dadkhah@gmail.com](mailto:pouria.dadkhah@gmail.com).

---
Feel free to explore the projects, use the code for your learning purposes, and contribute if you'd like to help improve the implementations!

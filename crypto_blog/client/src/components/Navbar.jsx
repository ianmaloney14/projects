const Navbar = (props) => {

    return (
        <div>
            <header className="header">
                <nav className="main-nav">
                    <ul className="main-nav-list">
                        <li><a className="main-nav-link">Education</a></li>
                        <li><a className="main-nav-link">Invest</a></li>
                        <li><a className="main-nav-link">Gamble</a></li>
                        <li><a className="main-nav-link">DeFi</a></li>
                        <li><a className="main-nav-link">NFT</a></li>
                        <li><a className="main-nav-link nav-cta">Best Crypto Tools</a></li>
                    </ul>
                </nav>
            </header>
        </div>
    )
}

export default Navbar;
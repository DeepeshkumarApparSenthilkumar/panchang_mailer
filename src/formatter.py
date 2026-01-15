def format_panchang_html(data):
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }}
            h2 {{ color: #d35400; text-align: center; }}
            .date {{ text-align: center; font-size: 1.2em; margin-bottom: 20px; color: #555; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ padding: 10px; text-align: left; border-bottom: 1px solid #eee; }}
            th {{ background-color: #f9f9f9; color: #7f8c8d; }}
            .highlight {{ color: #e67e22; font-weight: bold; }}
            .footer {{ margin-top: 20px; text-align: center; font-size: 0.8em; color: #999; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Daily Panchangam - Chicago</h2>
            <div class="date">{data.get('date', 'Unknown Date')}</div>
            
            <table>
                <tr><th>Sunrise</th><td>{data.get('sunrise', '-')}</td></tr>
                <tr><th>Sunset</th><td>{data.get('sunset', '-')}</td></tr>
                <tr><th>Moonrise</th><td>{data.get('moonrise', '-')}</td></tr>
                <tr><th>Moonset</th><td>{data.get('moonset', '-')}</td></tr>
                
                <tr><th>Tithi</th><td class="highlight">{data.get('tithi', '-')}</td></tr>
                <tr><th>Nakshatra</th><td class="highlight">{data.get('nakshatra', '-')}</td></tr>
                <tr><th>Yoga</th><td>{data.get('yoga', '-')}</td></tr>
                <tr><th>Karana</th><td>{data.get('karana', '-')}</td></tr>
                
                <tr><th>Rahu Kalam</th><td>{data.get('rahu_kalam', '-')}</td></tr>
                <tr><th>Yamaganda</th><td>{data.get('yamaganda', '-')}</td></tr>
                <tr><th>Abhijit Muhurta</th><td>{data.get('abhijit_muhurta', '-')}</td></tr>
                
                <tr><th>Sunsign</th><td>{data.get('sunsign', '-')}</td></tr>
                <tr><th>Moonsign</th><td>{data.get('moonsign', '-')}</td></tr>
            </table>
            
            <div class="footer">
                Data fetched from Drik Panchang for Chicago, IL.
            </div>
        </div>
    </body>
    </html>
    """
    return html

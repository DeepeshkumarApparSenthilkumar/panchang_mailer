def format_panchang_html(data):
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; background-color: #f4f4f4; padding: 20px; }}
            .container {{ max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); overflow: hidden; }}
            .header {{ background: linear-gradient(135deg, #d35400, #e67e22); color: white; padding: 20px; text-align: center; }}
            .header h2 {{ margin: 0; font-size: 24px; }}
            .header .date {{ font-size: 16px; margin-top: 5px; opacity: 0.9; }}
            .content {{ padding: 20px; }}
            
            .section-title {{ color: #d35400; font-size: 18px; margin-top: 20px; margin-bottom: 10px; border-bottom: 2px solid #eee; padding-bottom: 5px; }}
            
            .festival-box {{ background-color: #fff3cd; border-left: 5px solid #ffc107; padding: 15px; margin-bottom: 20px; border-radius: 4px; }}
            .festival-title {{ font-weight: bold; color: #856404; font-size: 16px; }}
            
            table {{ width: 100%; border-collapse: collapse; margin-bottom: 15px; }}
            th, td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #f0f0f0; }}
            th {{ background-color: #f9f9f9; color: #7f8c8d; width: 40%; font-weight: 600; }}
            td {{ color: #2c3e50; }}
            
            .highlight {{ color: #e67e22; font-weight: bold; }}
            .auspicious {{ color: #27ae60; font-weight: bold; }}
            .inauspicious {{ color: #c0392b; }}
            
            .footer {{ background-color: #f9f9f9; padding: 15px; text-align: center; font-size: 12px; color: #999; border-top: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>Daily Panchangam</h2>
                <div class="date">{data.get('date', 'Unknown Date')}</div>
                <div class="date" style="font-size: 14px; font-weight: normal;">{data.get('tamil_date', '')}</div>
            </div>
            
            <div class="content">
                <!-- Festivals Section -->
                <div class="festival-box">
                    <div class="festival-title">🎉 Festivals & Events</div>
                    <div>{data.get('festivals', 'No major festivals listed today.')}</div>
                </div>

                <div class="section-title">🌅 Sun & Moon</div>
                <table>
                    <tr><th>Sunrise</th><td>{data.get('sunrise', '-')}</td></tr>
                    <tr><th>Sunset</th><td>{data.get('sunset', '-')}</td></tr>
                    <tr><th>Moonrise</th><td>{data.get('moonrise', '-')}</td></tr>
                    <tr><th>Moonset</th><td>{data.get('moonset', '-')}</td></tr>
                </table>

                <div class="section-title">📅 Core Panchang</div>
                <table>
                    <tr><th>Tithi</th><td class="highlight">{data.get('tithi', '-')}</td></tr>
                    <tr><th>Nakshatra</th><td class="highlight">{data.get('nakshatra', '-')}</td></tr>
                    <tr><th>Yoga</th><td>{data.get('yoga', '-')}</td></tr>
                    <tr><th>Karana</th><td>{data.get('karana', '-')}</td></tr>
                </table>

                <div class="section-title">✨ Auspicious Timings</div>
                <table>
                    <tr><th>Abhijit Muhurta</th><td class="auspicious">{data.get('abhijit_muhurta', '-')}</td></tr>
                    <tr><th>Nalla Neram</th><td class="auspicious">{data.get('nalla_neram', '-')}</td></tr>
                    <tr><th>Gowri Nalla Neram</th><td class="auspicious">{data.get('gowri_nalla_neram', '-')}</td></tr>
                </table>

                <div class="section-title">⚠️ Inauspicious Timings</div>
                <table>
                    <tr><th>Rahu Kalam</th><td class="inauspicious">{data.get('rahu_kalam', '-')}</td></tr>
                    <tr><th>Yamaganda</th><td class="inauspicious">{data.get('yamaganda', '-')}</td></tr>
                </table>
                
                <div class="section-title">🔮 Astrology</div>
                <table>
                    <tr><th>Sunsign</th><td>{data.get('sunsign', '-')}</td></tr>
                    <tr><th>Moonsign</th><td>{data.get('moonsign', '-')}</td></tr>
                </table>
            </div>
            
            <div class="footer">
                Data fetched from Drik Panchang for Chicago, IL.<br>
                Automated by Deepesh Kumar
            </div>
        </div>
    </body>
    </html>
    """
    return html

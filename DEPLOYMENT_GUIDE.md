# Deployment Guide

This guide covers deploying your Plivo IVR demo to production environments.

---

## 🚀 Quick Deployment Options

| Platform | Difficulty | Free Tier | Best For |
|----------|-----------|-----------|----------|
| Heroku | Easy | Yes (limited) | Quick demos |
| Railway | Easy | Yes | Modern deployment |
| Render | Easy | Yes | Free hosting |
| DigitalOcean | Medium | No | Production apps |
| AWS EC2 | Advanced | Yes (12 months) | Enterprise |

---

## 1. Heroku Deployment

### Prerequisites
- Heroku account (https://signup.heroku.com/)
- Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
- Git repository initialized

### Steps

1. **Create a Procfile**

```bash
# In your project root
echo "web: gunicorn app:app" > Procfile
```

2. **Create runtime.txt** (specify Python version)

```bash
echo "python-3.11.0" > runtime.txt
```

3. **Login to Heroku**

```bash
heroku login
```

4. **Create Heroku App**

```bash
heroku create your-ivr-demo-app
# Note: Use a unique name
```

5. **Set Environment Variables**

```bash
heroku config:set PLIVO_AUTH_ID=your_auth_id
heroku config:set PLIVO_AUTH_TOKEN=your_auth_token
heroku config:set PLIVO_PHONE_NUMBER=your_plivo_number
heroku config:set ASSOCIATE_NUMBER=your_associate_number
heroku config:set BASE_URL=https://your-ivr-demo-app.herokuapp.com
```

6. **Deploy**

```bash
git add .
git commit -m "Initial deployment"
git push heroku main
```

7. **Open Your App**

```bash
heroku open
```

8. **View Logs** (for debugging)

```bash
heroku logs --tail
```

### Heroku Deployment Checklist
- [ ] Procfile created
- [ ] runtime.txt created
- [ ] All environment variables set
- [ ] BASE_URL updated with Heroku URL
- [ ] App deployed successfully
- [ ] Test call made successfully

---

## 2. Railway Deployment

### Prerequisites
- Railway account (https://railway.app/)
- GitHub account

### Steps

1. **Push Code to GitHub**

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/ivr-demo.git
git push -u origin main
```

2. **Deploy on Railway**

- Go to https://railway.app/
- Click "New Project"
- Select "Deploy from GitHub repo"
- Select your repository
- Railway auto-detects Python and deploys

3. **Add Environment Variables**

- Go to your project settings
- Click "Variables"
- Add each variable:
  - `PLIVO_AUTH_ID`
  - `PLIVO_AUTH_TOKEN`
  - `PLIVO_PHONE_NUMBER`
  - `ASSOCIATE_NUMBER`
  - `BASE_URL` (get from Railway after deployment)

4. **Get Your URL**

- Railway provides a URL like: `https://your-app.up.railway.app`
- Update `BASE_URL` variable with this URL

5. **Redeploy** (if needed)

- Push changes to GitHub
- Railway auto-deploys

### Railway Benefits
- Automatic HTTPS
- Free tier available
- Simple environment variable management
- Auto-deploys from GitHub

---

## 3. Render Deployment

### Prerequisites
- Render account (https://render.com/)
- GitHub account

### Steps

1. **Push Code to GitHub** (if not already done)

2. **Create Web Service on Render**

- Go to https://dashboard.render.com/
- Click "New +"
- Select "Web Service"
- Connect your GitHub repository

3. **Configure Service**

- **Name**: ivr-demo
- **Environment**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

4. **Add Environment Variables**

In the "Environment" section, add:
```
PLIVO_AUTH_ID=your_auth_id
PLIVO_AUTH_TOKEN=your_auth_token
PLIVO_PHONE_NUMBER=your_number
ASSOCIATE_NUMBER=your_associate_number
BASE_URL=https://your-app.onrender.com
```

5. **Deploy**

- Click "Create Web Service"
- Render will build and deploy automatically

6. **Update BASE_URL**

- Once deployed, get your Render URL
- Update the `BASE_URL` environment variable
- Service will auto-redeploy

---

## 4. DigitalOcean App Platform

### Prerequisites
- DigitalOcean account
- GitHub account

### Steps

1. **Create New App**

- Go to DigitalOcean dashboard
- Click "Apps" → "Create App"
- Connect GitHub repository

2. **Configure**

- Detected as Python app automatically
- Run Command: `gunicorn --bind 0.0.0.0:8080 app:app`

3. **Environment Variables**

Add all required variables in the App settings

4. **Deploy**

- App Platform builds and deploys
- Get your app URL
- Update `BASE_URL`

---

## 5. AWS EC2 (Advanced)

### Prerequisites
- AWS account
- SSH knowledge
- Domain name (optional)

### Steps

1. **Launch EC2 Instance**

- Ubuntu 22.04 LTS
- t2.micro (free tier eligible)
- Configure security group:
  - Port 22 (SSH)
  - Port 80 (HTTP)
  - Port 443 (HTTPS)

2. **Connect to Instance**

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

3. **Install Dependencies**

```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx -y
```

4. **Clone Your Repository**

```bash
git clone https://github.com/yourusername/ivr-demo.git
cd ivr-demo
```

5. **Set Up Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. **Create .env File**

```bash
nano .env
# Add your environment variables
```

7. **Install and Configure Gunicorn**

```bash
pip install gunicorn

# Create systemd service file
sudo nano /etc/systemd/system/ivr-demo.service
```

Add:
```ini
[Unit]
Description=Plivo IVR Demo
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/ivr-demo
Environment="PATH=/home/ubuntu/ivr-demo/venv/bin"
EnvironmentFile=/home/ubuntu/ivr-demo/.env
ExecStart=/home/ubuntu/ivr-demo/venv/bin/gunicorn --bind 0.0.0.0:8000 app:app

[Install]
WantedBy=multi-user.target
```

8. **Start Service**

```bash
sudo systemctl start ivr-demo
sudo systemctl enable ivr-demo
```

9. **Configure Nginx**

```bash
sudo nano /etc/nginx/sites-available/ivr-demo
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable:
```bash
sudo ln -s /etc/nginx/sites-available/ivr-demo /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

10. **SSL with Let's Encrypt** (optional)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Environment Variables Checklist

Regardless of platform, ensure these are set:

- [ ] `PLIVO_AUTH_ID` - From Plivo console
- [ ] `PLIVO_AUTH_TOKEN` - From Plivo console
- [ ] `PLIVO_PHONE_NUMBER` - Your Plivo number (E.164 format)
- [ ] `ASSOCIATE_NUMBER` - Number for call forwarding
- [ ] `BASE_URL` - Your deployment URL (HTTPS recommended)
- [ ] `PORT` - Usually auto-set by platform

---

## Post-Deployment Testing

1. **Test Web Interface**
   - Navigate to your deployed URL
   - Verify page loads correctly

2. **Test API Health**
   - Visit `https://your-url.com/health`
   - Should return JSON with status

3. **Test Call Flow**
   - Enter phone number
   - Initiate call
   - Verify webhooks work
   - Test all menu options

4. **Check Logs**
   - Monitor application logs
   - Watch for errors
   - Verify webhook requests

---

## Monitoring and Logs

### Heroku
```bash
heroku logs --tail
```

### Railway
- View logs in Railway dashboard
- Real-time log streaming

### Render
- Logs tab in service dashboard
- Automatic log retention

### AWS
```bash
sudo journalctl -u ivr-demo -f
```

---

## Troubleshooting Deployment Issues

### Issue: Webhooks Not Working

**Cause**: BASE_URL not updated or incorrect

**Solution**:
1. Get your deployment URL
2. Update BASE_URL environment variable
3. Ensure URL uses HTTPS (Plivo requirement for production)
4. Restart/redeploy application

### Issue: Application Won't Start

**Cause**: Missing dependencies or environment variables

**Solution**:
1. Check logs for specific error
2. Verify all environment variables are set
3. Ensure requirements.txt includes all dependencies
4. Check Python version compatibility

### Issue: 502 Bad Gateway

**Cause**: Application not running or wrong port

**Solution**:
1. Check application logs
2. Verify port binding (use 0.0.0.0, not localhost)
3. Restart the service

### Issue: SSL/HTTPS Problems

**Cause**: Plivo requires HTTPS for production webhooks

**Solution**:
1. Use platform's automatic HTTPS (Heroku, Railway, Render all provide this)
2. Or set up Let's Encrypt (for custom servers)
3. Ensure BASE_URL uses https://

---

## Security Best Practices

1. **Never Commit Secrets**
   - Use `.gitignore` for `.env`
   - Use environment variables for all secrets

2. **Use HTTPS**
   - Required for production Plivo webhooks
   - Most platforms provide this automatically

3. **Rotate Credentials**
   - Regularly update Plivo auth tokens
   - Use strong, unique passwords

4. **Rate Limiting**
   - Consider adding rate limiting to prevent abuse
   - Limit calls per IP/user

5. **Input Validation**
   - Already implemented in the app
   - Keep validation strict

---

## Scaling Considerations

For production use:

1. **Database**: Add PostgreSQL for call logs
2. **Caching**: Use Redis for session management
3. **Queue**: Use Celery for async call handling
4. **Monitoring**: Add Sentry for error tracking
5. **Analytics**: Track call metrics

---

## Cost Estimates

### Free Tiers (Suitable for Demo)
- **Heroku**: 550 hours/month free
- **Railway**: $5 free credit/month
- **Render**: Free for web services (with limitations)

### Plivo Costs
- Phone number: ~$1/month
- Outbound calls: ~$0.01/minute
- Trial account: Free credits

### Recommendations
- Use free tier platforms for demo
- Monitor Plivo usage
- Set up billing alerts

---

## Deployment Checklist

- [ ] Code pushed to repository
- [ ] Environment variables configured
- [ ] BASE_URL updated with deployment URL
- [ ] Application deployed successfully
- [ ] Health check endpoint works
- [ ] Web interface accessible
- [ ] Test call completes successfully
- [ ] All menu options work
- [ ] Logs accessible for debugging
- [ ] Demo video recorded
- [ ] Documentation updated

---

## Support Resources

- **Heroku**: https://devcenter.heroku.com/
- **Railway**: https://docs.railway.app/
- **Render**: https://render.com/docs
- **Plivo**: https://www.plivo.com/docs/
- **Flask**: https://flask.palletsprojects.com/

---

**You're ready to deploy! Choose the platform that best fits your needs and follow the steps above.** 🚀

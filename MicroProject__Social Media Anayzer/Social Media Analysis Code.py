import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
df = pd.read_csv("social_media_usage.csv") 
while True: 
    print("\n========== SOCIAL MEDIA USAGE ANALYSIS ==========") 
    print("1.Dataset Information") 
    print("2.Missing Values") 
    print("3.Basic Statistics") 
    print("4.Usage by App")
    print("5.Likes by App")
    print("6.Posts by App")
    print("7.App Usage Distribution") 
    print("8.Usage vs Likes Analysis") 
    print("9.Correlation Analysis")
    print("10.Correlation Heatmap") 
    print("11.Usage Statistics by App") 
    print("12.Predict Daily Minutes Spent") 
    print("13.Average daily usage by app") 
    print("14.App Usage Distribution") 
    print("15.App-wise Comparison") 
    print("16.exit")
    choice = int(input("\nEnter your choice: "))  
    match choice:
        case 1:
            print("\n========== DATASET INFORMATION ==========")
            print("\nFirst 5 Records:")
            print(df.head())
            print("\nDataset Shape:")
            print(df.shape)
            print("\nColumn Names:") 
            print(df.columns)
            print("\nData Types:")
            print(df.dtypes)
        case 2: 
            print("\n========== MISSING VALUES ==========")
            print(df.isnull().sum())
        case 3: 
            print("\n========== BASIC STATISTICS ==========")
            print(df.describe())
        case 4: 
            print("\n========== AVERAGE USAGE BY APP ==========")
            usage = df.groupby("App")["Daily_Minutes_Spent"].mean()
            print(usage)
        case 5: 
            print("\n========== AVERAGE LIKES BY APP ==========")
            likes = df.groupby("App")["Likes_Per_Day"].mean()
            print(likes)
        case 6: 
            print("\n========== AVERAGE POSTS BY APP ==========")
            posts = df.groupby("App")["Posts_Per_Day"].mean()
            print(posts)
        case 7:
            print("\n========== APP USAGE DISTRIBUTION ==========")
            plt.figure(figsize=(8, 5))
            plt.hist(df["Daily_Minutes_Spent"],bins=10,edgecolor="black")
            plt.title("Distribution of Daily Social Media Usage")
            plt.xlabel("Daily Usage (Minutes)")
            plt.ylabel("Number of Users")
            plt.grid(axis="y", alpha=0.3) 
            plt.show() 
        case 8:
            print("\n========== USAGE VS LIKES ANALYSIS ==========") 
            plt.figure(figsize=(8, 5))
            sns.scatterplot(data=df,x="Daily_Minutes_Spent",y="Likes_Per_Day",hue="App",s=80)
            plt.title("Daily Social Media Usage vs Likes")
            plt.xlabel("Daily Usage (Minutes)")
            plt.ylabel("Likes Per Day")
            plt.grid(True, alpha=0.3)
            plt.show()
        case 9:
            print("\n========== CORRELATION ANALYSIS ==========")
            corr = df[["Daily_Minutes_Spent","Posts_Per_Day","Likes_Per_Day","Follows_Per_Day"]].corr()
            print(corr)
        case 10:
            print("\n========== CORRELATION HEATMAP ==========")
            corr = df[["Daily_Minutes_Spent","Posts_Per_Day","Likes_Per_Day","Follows_Per_Day"]].corr()
            plt.figure(figsize=(8, 6))
            sns.heatmap(corr,annot=True,cmap="Spectral")
            plt.title("Correlation Heatmap")
            plt.show()
        case 11:
            print("\n========== USAGE STATISTICS BY APP ==========")
            app_stats = df.groupby("App")["Daily_Minutes_Spent"].agg(["mean", "min", "max", "count"])
            print(app_stats)
        case 12:
            print("\n========== PREDICT DAILY MINUTES SPENT ==========")
            app_data = df.groupby("App").agg({"Daily_Minutes_Spent": "mean","Posts_Per_Day": "mean","Likes_Per_Day": "mean","Follows_Per_Day": "mean"})
            print("\nEnter details for prediction:")
            app = input("Enter App: ")
            posts = float(input("Enter Posts Per Day: "))
            likes = float(input("Enter Likes Per Day: "))
            follows = float(input("Enter Follows Per Day: "))
            matching_app = [x for x in app_data.index if x.lower() == app.lower()]
            if len(matching_app) == 0:
                print("\nApp not found in dataset.")
            else:
                selected_app = matching_app[0]
                avg_minutes = app_data.loc[selected_app, "Daily_Minutes_Spent"]
                avg_posts = app_data.loc[selected_app, "Posts_Per_Day"]
                avg_likes = app_data.loc[selected_app, "Likes_Per_Day"]
                avg_follows = app_data.loc[selected_app, "Follows_Per_Day"]
                posts_factor = posts / avg_posts
                likes_factor = likes / avg_likes
                follows_factor = follows / avg_follows
                activity_factor = (posts_factor +likes_factor +follows_factor) / 3
                predicted_minutes = avg_minutes * activity_factor
                print("\n========== PREDICTION RESULT ==========")
                print("App:", selected_app)
                print("Posts Per Day:", posts)
                print("Likes Per Day:", likes)
                print("Follows Per Day:", follows)
                print("Predicted Daily Minutes:",round(predicted_minutes, 2),"minutes")
        case 13:
            print("\n========== AVERAGE USAGE BY APP ==========")
            usage = df.groupby("App")["Daily_Minutes_Spent"].mean()
            print(usage.round(2))
            plt.figure(figsize=(8, 5))
            usage.plot(kind="bar")
            plt.title("Average Daily Usage by App")
            plt.xlabel("Social Media App")
            plt.ylabel("Average Usage (Minutes)")
            plt.xticks(rotation=45)
            plt.grid(axis="y", alpha=0.3)
            plt.show()
        case 14:
            print("\n========== APP USAGE DISTRIBUTION ==========")
            app_count = df["App"].value_counts()
            print("\nNumber of Users by App:")
            print(app_count)  
            plt.figure(figsize=(8, 6)) 
            plt.pie(app_count,labels=app_count.index,autopct="%1.1f%%",startangle=90)
            plt.title("Social Media App Usage Distribution")
            plt.show()
        case 15:
            print("\n========== APP-WISE COMPARISON ==========")
            app_analysis = df.groupby("App").agg({"Daily_Minutes_Spent": "mean","Posts_Per_Day": "mean","Likes_Per_Day": "mean","Follows_Per_Day": "mean"})
            print(app_analysis.round(2))
            app_analysis.plot(kind="bar",figsize=(10, 6))
            plt.title("App-wise Social Media Activity")
            plt.xlabel("Social Media App")
            plt.ylabel("Average Value")
            plt.xticks(rotation=1)
            plt.legend(title="Activity")
            plt.show()
        case 16:
            print("\nThank you for using Social Media Usage Analysis!")
            break
        case _:
            print("\nInvalid choice! Please enter a number from 1 to 15.")

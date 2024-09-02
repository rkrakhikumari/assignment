import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from data_processing import generate_user_report, calculate_total_spent, calculate_average_transaction_amount


app = dash.Dash(__name__)


report_df = generate_user_report()
total_spent_df = calculate_total_spent()
average_transaction_df = calculate_average_transaction_amount()


top_users = report_df.sort_values(by='total_spent', ascending=False).head(3)
fig1 = px.bar(top_users, x='name', y='total_spent', title='Top 3 Users by Total Amount Spent')
fig2 = px.line(total_spent_df, x='user_id', y='total_spent', title='Total Amount Spent by Each User')


app.layout = html.Div([
    html.H1("User Data Dashboard"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    html.H2(f"Average Transaction Amount: {average_transaction_df.iloc[0]['average_transaction_amount']:.2f}"),
    html.Table([
        html.Thead(html.Tr([html.Th(col) for col in report_df.columns])),
        html.Tbody([
            html.Tr([html.Td(report_df.iloc[i][col]) for col in report_df.columns])
            for i in range(len(report_df))
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
